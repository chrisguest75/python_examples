# ELASTICSEARCH

Demonstrate a simple elasticsearch example.

NOTES:

- Kibana Stack Management -> Index Management -> Indices
- Create a data view

## Elasticsearch

```sh
docker network create elastic

docker run --rm -p 9200:9200 -d --net elastic --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.security.http.ssl.enabled=false" \
  -e "xpack.license.self_generated.type=basic" \
  docker.elastic.co/elasticsearch/elasticsearch:8.12.1

docker run --rm --env-file elastic.env --net elastic --name kibana -p 5601:5601 docker.elastic.co/kibana/kibana:8.12.1

open http://0.0.0.0:9200
open http://0.0.0.0:5601
```

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run lint
pipenv run test

# enter venv
pipenv shell

# create .env file
cp .env.template .env

# run with arguments
pipenv run start --test
pipenv run start:test
```

## Cleanup

```sh
docker stop elasticsearch
docker stop kibana
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Created

```sh
# install
pyenv global 3.11.1
pipenv install
pipenv install --dev flake8 flake8-bugbear flake8-2020 black
pipenv install --dev pytest
pipenv install pyyaml python-json-logger python-dotenv

pipenv install elasticsearch
```

## Resources

- Search Tutorial [here](https://www.elastic.co/search-labs/tutorials/search-tutorial/welcome)
- elastic/elasticsearch docker examples [here](https://github.com/elastic/elasticsearch/tree/8.12/docs/reference/setup/install/docker)
