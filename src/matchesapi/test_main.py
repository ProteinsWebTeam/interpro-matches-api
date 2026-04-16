import tarfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from rocksdict import AccessType, Options, Rdict

from .main import Settings, create_app, get_db


FOUND_MD5 = "019E72422B4EBA0F352981C70C23F123"
FOUND_MD5_NO_MATCHES = "00018A5371E8F55E04121A619974B990"
MISSING_MD5 = "F1CFB8647A4FAE6E980293E1F4085680"



@pytest.fixture(scope="session")
def minidb_path(tmp_path_factory: Path) -> Path:
    root = tmp_path_factory.mktemp("matchesapi-data")
    archive = Path("data/minidb.tar.gz")
    with tarfile.open(archive, "r:gz") as tf:
        tf.extractall(root)
    return root / "minidb"


@pytest.fixture(scope="session")
def test_db(minidb_path: Path):
    db = Rdict(
        str(minidb_path),
        access_type=AccessType.read_only(),
        options=Options(raw_mode=True),
    )
    yield db
    db.close()


@pytest.fixture
def client(minidb_path: Path, test_db: Rdict):
    app = create_app(settings=Settings(path=minidb_path, limit=100), db=test_db)
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as test_client:
        yield test_client


def test_single_md5_found(client):
    response = client.get(f"/matches/{FOUND_MD5}")
    assert response.status_code == 200
    payload = response.json()
    assert payload["md5"] == FOUND_MD5
    assert len(payload["matches"]) > 0


def test_single_md5_found_no_matches(client):
    response = client.get(f"/matches/{FOUND_MD5_NO_MATCHES}")
    assert response.status_code == 200
    payload = response.json()
    assert payload["md5"] == FOUND_MD5_NO_MATCHES
    assert len(payload["matches"]) == 0


def test_single_md5_not_found(client):
    response = client.get(f"/matches/{MISSING_MD5}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Sequence not found"}


def test_batch_deduplicates_and_marks_missing(client):
    response = client.post(
        "/matches",
        json={"md5": [FOUND_MD5, FOUND_MD5, MISSING_MD5, FOUND_MD5_NO_MATCHES]},
    )

    assert response.status_code == 200
    payload = response.json()
    results = payload["results"]
    assert len(results) == 3
    for result in results:
        md5 = result["md5"]
        found = result["found"]
        matches = result["matches"]
        assert md5 in {FOUND_MD5, MISSING_MD5, FOUND_MD5_NO_MATCHES}
        
        if md5 == FOUND_MD5:
            assert found is True
            assert len(matches) > 0
        elif md5 == MISSING_MD5:
            assert found is False
            assert len(matches) == 0
        else:
            assert found is True
            assert len(matches) == 0

