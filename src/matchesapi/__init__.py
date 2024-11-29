import importlib.metadata
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, DirectoryPath, constr, conlist

from rocksdict import Rdict, AccessType, Options
from . import examples


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MATCHES_API_")
    path: DirectoryPath
    debug: bool = False
    info: dict = {}


settings = Settings()
db = Rdict(str(settings.path),
           access_type=AccessType.read_only(),
           options=Options(raw_mode=True))
app = FastAPI(
    title="InterPro Matches API",
    description="""
The Matches API provides access to pre-calculated InterProScan results for \
all sequences in UniParc.

When InterProScan is queried with a known sequence, it retrieves the result \
from the Matches API and reports the result immediately, thereby reducing \
compute requirements and improving performance.""",
    version=importlib.metadata.version("interpro-matches-api"),
    terms_of_service="https://www.ebi.ac.uk/about/terms-of-use",
    contact={
        "name": "InterPro helpdesk",
        "url": "https://www.ebi.ac.uk/about/contact/support/interpro",
    },
    # Docs URLs
    docs_url="/docs",  # default
    redoc_url=None,    # disable ReDoc

)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    with (settings.path / "interpro.json").open("rt") as fh:
        settings.info.update(json.load(fh))


@app.on_event("shutdown")
async def on_shutdown():
    db.close()


@app.get("/about", include_in_schema=False)
async def about():
    return settings.info


class MD5sQuery(BaseModel):
    md5: conlist(constr(to_upper=True, min_length=32, max_length=32),
                 min_length=1, max_length=1000)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "md5": list(examples.matches.keys())
                }
            ]
        }
    }


@app.post("/matches", responses=examples.matches_responses)
async def matches(query: MD5sQuery) -> dict[str, list[dict] | None]:
    results = {}
    for md5 in query.md5:
        if md5 not in results:
            value = db.get(md5.encode("utf-8"))
            results[md5] = None if value is None else json.loads(value)

    return results
