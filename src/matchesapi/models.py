from pydantic import BaseModel, Field, constr, conlist

from .examples import matches


class LocationFragment(BaseModel):
    start: int
    end: int
    dc_status: str = Field(..., alias="dc-status")


class SiteLocation(BaseModel):
    start: int
    end: int
    residue: str


class Site(BaseModel):
    description: str
    numLocations: int
    siteLocations: list[SiteLocation]


class Location(BaseModel):
    start: int
    end: int
    hmmStart: int
    hmmEnd: int
    hmmLength: int
    hmmBounds: str | None
    envelopeStart: int
    envelopeEnd: int
    evalue: float
    score: float
    location_fragments: list[LocationFragment] = Field(..., alias="location-fragments")
    sequence_feature: str | None = Field(None, alias="sequence-feature")
    sites: list[Site]


class Entry(BaseModel):
    accession: str
    name: str
    description: str
    type: str
    parent: str | None


class SignatureLibraryRelease(BaseModel):
    library: str
    version: str


class Signature(BaseModel):
    accession: str
    name: str | None
    description: str | None
    signatureLibraryRelease: SignatureLibraryRelease
    entry: Entry | None


class Match(BaseModel):
    signature: Signature
    model_ac: str = Field(..., alias="model-ac")
    score: float
    evalue: float
    locations: list[Location]


class SingleResponse(BaseModel):
    md5: str
    matches: list[Match]


class BatchResult(SingleResponse):
    found: bool


class BatchResponse(BaseModel):
    results: list[BatchResult]


class BatchSearchQuery(BaseModel):
    md5: conlist(
        constr(to_upper=True, min_length=32, max_length=32),
        min_length=1,
        max_length=1000,
    )

    model_config = {
        "json_schema_extra": {"examples": [{"md5": [m["md5"] for m in matches]}]}
    }
