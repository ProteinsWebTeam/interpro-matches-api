# InterPro Matches API

The InterPro Matches API provides programmatic access to pre-computed [InterProScan 6](https://github.com/ebi-pf-team/interproscan6/) results 
for every sequence in [UniParc](https://www.uniprot.org/uniparc/). Each UniParc sequence is identified by its MD5 hash, 
which serves as a unique key for fast lookups of its associated InterPro matches.

When InterProScan runs, it computes the MD5 hash of each input sequence and queries this API. 
If the sequence is already in UniParc, the pre-calculated results are returned immediately—saving 
compute time and resources. Although this API was created to speed up InterProScan, 
you can also use it directly: submit up to 100 MD5 hashes in a single request 
and retrieve their InterPro matches in bulk.

## Usage

### Getting the data

Fetch the latest archive and its MD5 checksum:

```sh
curl -OJ https://ftp.ebi.ac.uk/pub/databases/interpro/releases/latest/matches-api-data.tar.gz
curl -OJ https://ftp.ebi.ac.uk/pub/databases/interpro/releases/latest/matches-api-data.tar.gz.md5
```

Verify integrity:

```sh
md5sum -c matches-api-data.tar.gz.md5  
# you should see: matches-api-data.tar.gz: OK
```

Create a `matches-api-data` directory and unpack the archive into it:

```sh
mkdir matches-api-data  
tar -zxvf matches-api-data.tar.gz \
    --strip-components=1 \
    -C matches-api-data
```

### Starting the API server

#### With Docker

```sh
docker run --rm \
  -v $PWD/matches-api-data:/data \
  -e MATCHES_API_PATH=/data \
  -p 8000:8000 \
  interpro/matches-api:0.4.0
```

#### With Singularity

Optionally set your cache and Docker Hub credentials first:

```sh
export SINGULARITY_CACHEDIR="/path/to/cache/dir"
export SINGULARITY_DOCKER_USERNAME="username"
export SINGULARITY_DOCKER_PASSWORD="personal-access-token"
  ```

Then run:

```sh
singularity run \
    -B $PWD/matches-api-data:/data \
    --env "MATCHES_API_PATH=/data" \
    docker://interpro/matches-api:0.4.0
```

### Querying the running API

The server listens on port `8000`. To fetch matches for multiple MD5 hashes:

```sh
curl -X POST "api-host:8000/matches" -H 'Content-Type: application/json' -d'
{
  "md5": [
    "020DA9322D8466E699BDD584593749FC",
    "0204A4724F5991CB9B7E1013CBDA3367",
    "00C5D66EC4232D18A9639ECF3FC4BDDB"
  ]
}
' | jq
```

## Local development

Clone the repository and install in editable mode:

```sh
pip install -e .
```

Extract the test database (included under `data/minidb.tar.gz`):

```sh
tar -C data -zxf data/minidb.tar.gz
```

Point the server to that database and launch it:

```sh
export MATCHES_API_PATH="data/minidb"
uvicorn matchesapi.main:app
```
