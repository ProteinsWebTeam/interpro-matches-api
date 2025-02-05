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
curl -X POST "localhost:8000/search" -H 'Content-Type: application/json' -d'
{
  "md5s": [
    "D807BE58521078C19090570C3170B91F",
    "72A998E920EEC132301E6A5EB4BCD4CE",
    "A4244BE42EC787C383263F876D38720C"
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
# Optional
export SINGULARITY_DOCKER_USERNAME=<username>
export SINGULARITY_DOCKER_PASSWORD=<personal-access-token>
 
singularity run \
    -B $PWD/data/minidb:/data \
    --env "MATCHES_API_PATH=/data" \
    docker://interpro/matches-api:latest
```