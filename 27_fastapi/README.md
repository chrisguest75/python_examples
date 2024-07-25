# 27_fastapi

Demonstrate fastapi

TODO:

* dockerise
* add proper api
* uvicorn
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

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

* FastAPI framework, high performance, easy to learn, fast to code, ready for production [here](https://fastapi.tiangolo.com/#installation)
