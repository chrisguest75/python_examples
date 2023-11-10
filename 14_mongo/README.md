# MONGODB

To create follow repository [README.md](../README.md)  

TODO:

* Load a dataset using faker
* Query a dataset find users in orgs

## 🏠 Start

```sh
pipenv install --dev
```

## Startup Mongo

```sh
# list profiles
docker compose config --profiles

# start mongo (profiles not working at the mo')
# It is working in compose: Docker Compose (Docker Inc., v2.0.0-beta.6) - Docker Desktop 3.5.2
docker compose --profile backend up -d 

# quick test
docker logs $(docker ps --filter name=14_monogo-mongodb-1 -q)
```

## Rebuild backend and run

```sh
# if changes are made to backend rerun
docker-compose --profile backend up -d --build
```

## Query

```sh
# load values from env file
. ./.env  
# run the query
pipenv run start --mongo ${MONGO_CONNECTION} --query ./queries/query1.json --db ${MONGO_DB} --collection ${MONGO_COLLECTION}
```

## Resources

* https://pymongo.readthedocs.io/en/stable/
* https://github.com/joke2k/faker