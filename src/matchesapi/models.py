from pydantic import BaseModel, constr, conlist

from .examples import matches


class LocationFragment(BaseModel):
    start: int
    end: int
    type: str


class SiteLocation(BaseModel):
    start: int
    end: int
    residue: str


class Site(BaseModel):
    description: str | None
    numLocations: int
    siteLocations: list[SiteLocation]


class Location(BaseModel):
    start: int
    end: int
    fragments: list[LocationFragment]
    hmmStart: int | None = None
    hmmEnd: int | None = None
    hmmLength: int | None = None
    hmmBounds: str | None = None
    envelopeStart: int | None = None
    envelopeEnd: int | None = None
    evalue: float | None = None
    score: float | None = None
    sequenceFeature: str | None = None
    sites: list[Site] | None = None
    pvalue: float | None = None
    motifNumber: int | None = None
    cigarAlignment: str | None = None


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
    modelAccession: str
    locations: list[Location]
    score: float | None = None
    evalue: float | None = None
    annotationNode: str | None = None
    graphscan: str | None = None


class SingleResponse(BaseModel):
    md5: str
    matches: list[Match]


class BatchResult(SingleResponse):
    found: bool


class BatchResponse(BaseModel):
    results: list[BatchResult]


class BatchQuery(BaseModel):
    md5: conlist(
        constr(to_upper=True, min_length=32, max_length=32),
        min_length=1,
        max_length=1000,
    )

    model_config = {
        "json_schema_extra": {"examples": [{"md5": [m["md5"] for m in matches]}]}
    }
