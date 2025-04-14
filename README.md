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
uvicorn matchesapi.main:app
```

Query the matches for a few MD5 hashes:

```sh
curl -X POST "localhost:8000/search" -H 'Content-Type: application/json' -d'
{
  "md5": [
    "020DA9322D8466E699BDD584593749FC",
    "0204A4724F5991CB9B7E1013CBDA3367",
    "00C5D66EC4232D18A9639ECF3FC4BDDB"
  ]
}
' | python -m json.tool
```

## Test database

A test database is provided in `data` as a compressed/split `tar` archive.
To extract it, run the following:

```sh
tar -C data -zxf data/minidb.tar.gz
```

### With Docker or Singularity

<details>
  <summary>Build Docker image (optional)</summary>

  ```sh
  docker build --no-cache -t interpro/matches-api:latest .
  ```
</details>

Start Docker container:

```sh
docker run --rm \
  -v $PWD/data/minidb:/data \
  -e MATCHES_API_PATH=/data \
  -p 8000:8000 \
  interpro/matches-api:latest
```

Start Singularity container:

```sh
singularity run \
    -B $PWD/data/minidb:/data \
    --env "MATCHES_API_PATH=/data" \
    docker://interpro/matches-api:latest
```