import importlib.metadata
import json
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, DirectoryPath, constr, conlist
from rocksdict import Rdict, AccessType, Options

from . import models, examples


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MATCHES_API_")
    path: DirectoryPath
    limit: int = 100
    debug: bool = False
    info: dict = {"api": importlib.metadata.version("interpro-matches-api")}


settings = Settings()


class BatchQuery(BaseModel):
    md5: conlist(models.MD5String, min_length=1, max_length=settings.limit)

    model_config = {
        "json_schema_extra": {
            "examples": [{"md5": [m["md5"] for m in examples.matches]}]
        }
    }


db = Rdict(
    str(settings.path),
    access_type=AccessType.read_only(),
    options=Options(raw_mode=True),
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    with (settings.path / "interpro.json").open("rt") as fh:
        settings.info.update(json.load(fh))
    yield
    db.close()


app = FastAPI(
    title="InterPro Matches API",
    description=f"""
The Matches API provides access to pre-calculated \
[InterProScan](https://www.ebi.ac.uk/interpro/search/sequence/) results for \
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
of up to {settings.limit:,} sequences in a single request to quickly and \
efficiently access pre-calculated match results.""",
    version=importlib.metadata.version("interpro-matches-api"),
    terms_of_service="https://www.ebi.ac.uk/about/terms-of-use",
    contact={
        "name": "InterPro helpdesk",
        "url": "https://www.ebi.ac.uk/about/contact/support/interpro",
    },
    # Docs URLs
    docs_url="/",  # default
    redoc_url=None,  # disable ReDoc
    # Start/shutdown events
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/matches/{md5}",
    name="Single MD5",
    description="Get InterPro matches by sequence MD5 checksum",
    response_model=models.SingleResponse,
    responses=examples.single_responses,
    response_model_exclude_unset=True,
)
async def single(md5: constr(to_upper=True, min_length=32, max_length=32)) -> Any:
    """
    Search for a single MD5 hash using a URL parameter.
    """
    value = db.get(md5.encode("utf-8"))
    if value is None:
        raise HTTPException(status_code=404, detail="Sequence not found")

    return {"md5": md5, "matches": json.loads(value)}


@app.post(
    "/matches",
    name="Multiple MD5",
    description="Get InterPro matches for multiple sequence MD5 checksums",
    response_model=models.BatchResponse,
    response_model_exclude_unset=True,
)
async def batch(query: BatchQuery) -> Any:
    results = {}
    for md5 in query.md5:
        if md5 not in results:
            value = db.get(md5.encode("utf-8"))
            if value is None:
                found = False
                matches = []
            else:
                found = True
                matches = json.loads(value)

            results[md5] = {"md5": md5, "found": found, "matches": matches}

    return {"results": list(results.values())}


@app.get("/health", include_in_schema=False)
async def health():
    try:
        with (settings.path / "interpro.json").open("rt") as fh:
            obj = json.load(fh)
    except FileNotFoundError:
        raise HTTPException(status_code=503, detail="Service not ready")

    if obj["release"] == settings.info["release"]:
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=503, detail="Service not ready")


@app.get("/info", include_in_schema=False)
async def info():
    return settings.info
