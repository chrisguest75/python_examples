# POETRY

Demonstrates:

- flake8 linting
- logging
- argument parsing
- docstrings

NOTES:

- Check with pyenv that the version is installed. `pyenv install` 

TODO:

- It's not working - when you do run it fails to find pyyaml
- being able to run scripts
- run tests
- poetry run python main.py

## Install

```sh
brew install poetry
```

## Start

```sh
export POETRY_VIRTUALENVS_IN_PROJECT=1
export POETRY_VIRTUALENVS_CREATE=1

# install
pyenv install
poetry install

# lint and test code
poetry run lint
poetry run test

# enter venv
poetry shell

# create .env file
cp .env.template .env

# run with arguments
poetry run start --test
poetry run start:test
```

## Debugging and Troubleshooting

```sh
# enter python
poetry run python

> import main

> main.test.__doc__
```

## Created

```sh
# install
poetry init
poetry config --local virtualenvs.create true
poetry config --local virtualenvs.in-project true

poetry add --group dev flake8 flake8-bugbear flake8-2020 black
poetry add --group dev pytest
poetry add pyyaml python-json-logger python-dotenv


##
echo "3.11.1" > .python-version
poetry env use python3.11


```

## Resources

- Poetry is a tool for dependency management and packaging in Python. [here](https://python-poetry.org/docs/)
- Build Command Line Tools with Python Poetry [here](https://dev.to/bowmanjd/build-command-line-tools-with-python-poetry-4mnc)
- I move from pipenv to poetry in 2023 - Am I right ? [here](https://dev.to/farcellier/i-migrate-to-poetry-in-2023-am-i-right--115)
- PyEnv & Poetry - BFFs [here](https://dev.to/mattcale/pyenv-poetry-bffs-20k6)
