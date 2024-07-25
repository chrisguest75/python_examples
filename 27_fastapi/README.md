# 27_fastapi

Demonstrate fastapi

TODO:

* pydantic

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
pipenv run start:fastapi
```

## Docker

```sh
pipenv run build:docker
pipenv run start:docker

open http://127.0.0.1:8000/
open http://127.0.0.1:8000/docs
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

* FastAPI framework, high performance, easy to learn, fast to code, ready for production [here](https://fastapi.tiangolo.com/#installation)
* An ASGI web server, for Python. [here](https://www.uvicorn.org/)
