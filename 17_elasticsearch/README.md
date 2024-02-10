# ELASTICSEARCH

Demonstrate a simple elasticsearch example.

## Elasticsearch

```sh
docker run -p 9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.security.http.ssl.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  docker.elastic.co/elasticsearch/elasticsearch:8.11.0

open http://localhost:9200
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

- https://www.elastic.co/search-labs/tutorials/search-tutorial/welcome
