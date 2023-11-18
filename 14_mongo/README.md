# MONGODB

To create follow repository [README.md](../README.md)  

TODO:

* Query a dataset find users in orgs
* Load data from aws batch jobs and load into mongo to keep
* Split into classes to do data loading

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

## Connect to mongosh

```sh
mongosh "mongodb://root:rootpassword@0.0.0.0:27017/"

show dbs

mongosh "mongodb://mongouser:mongopassword@/0.0.0.0:27017/"


db.getCollection('jobs').find({})
```




## Query

```sh
# run the query
pipenv run start --process=load_batch_jobs --config ./configs/config.localmongo.dev.json
```

## Shutdown

```sh
docker compose --profile backend down   
```

## Resources

* https://pymongo.readthedocs.io/en/stable/
* https://github.com/joke2k/faker
* https://github.com/chrisguest75/mongo_examples/blob/main/03_ffprobe/README.md