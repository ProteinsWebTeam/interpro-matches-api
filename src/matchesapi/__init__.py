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
all sequences in [UniParc](https://www.uniprot.org/uniparc/).

Each sequence in UniParc is assigned a unique identifier \
using the MD5 hashing method. This ensures that every sequence has a distinct \
MD5, which serves as a key to quickly and efficiently retrieve \
its corresponding InterPro matches.

InterProScan uses the Matches API to streamline sequence analysis. \
It calculates the MD5 for each input sequence and queries the Matches API \
to fetch pre-calculated results for sequences already present in UniParc. \
This approach eliminates redundant computations, \
saving resources and improving overall performance.

While the Matches API was primarily designed to enhance the efficiency \
of InterProScan, it is also available to researchers and other services \
seeking to retrieve InterPro matches. Users can submit the MD5 identifiers \
of up to 1,000 sequences in a single request to quickly and efficiently \
access pre-calculated match results.""",
    version=importlib.metadata.version("interpro-matches-api"),
    terms_of_service="https://www.ebi.ac.uk/about/terms-of-use",
    contact={
        "name": "InterPro helpdesk",
        "url": "https://www.ebi.ac.uk/about/contact/support/interpro",
    },
    # Docs URLs
    docs_url="/",    # default
    redoc_url=None,  # disable ReDoc

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
    md5s: conlist(constr(to_upper=True, min_length=32, max_length=32),
                  min_length=1, max_length=1000)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "md5s": list(examples.matches.keys())
                }
            ]
        }
    }


@app.post("/search", responses=examples.matches_responses)
async def matches(query: MD5sQuery) -> dict[str, list[dict] | None]:
    results = {}
    for md5 in query.md5s:
        if md5 not in results:
            value = db.get(md5.encode("utf-8"))
            results[md5] = None if value is None else json.loads(value)

    return results
