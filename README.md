# InterPro Matches API

## Getting stated

Clone and install the package:

```sh
pip install .
```

## Start the API

Specify the path to the database, then start the server:

```sh
export MATCHES_API_PATH="/path/to/database"
uvicorn matchesapi:app
```

Query the matches for a few MD5 hashes:

```sh
curl -X POST "localhost:8000/matches" -H 'Content-Type: application/json' -d'
{
  "md5": [
    "5FE1059FDE57D6E61C5343CAB0C502C8",
    "706475FD3508BACF05958AC1D6C7B9BD",
    "B5437FBB59FED6ED5A1A0F7B3409A5D0"
  ]
}
' | python -m json.tool
```

## Test database

A test database is provided in `data` as a compressed/split `tar` archive.
To extract it, run the following:

```sh
cat data/minidb* | tar -C data -zxf -
```

### With Docker

<details>
  <summary>Build image (optional)</summary>

  ```sh
  docker build --no-cache -t interpro/matches-api:latest .
  ```
</details>

Start server:

```sh
docker run --rm \
  -v $PWD/data/minidb:/data \
  -e MATCHES_API_PATH=/data \
  -p 8000:8000 \
  interpro/matches-api:latest
```
