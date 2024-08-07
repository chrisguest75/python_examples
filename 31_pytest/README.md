# 31_pytest

Demonstrate 31_pytest

TODO:

- pytest --fixtures
- pymock

## Contents

- [31_pytest](#31_pytest)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [pytest](#pytest)
  - [Debugging and Troubleshooting](#debugging-and-troubleshooting)
    - [Interpreter](#interpreter)
    - [Pipenv Environment](#pipenv-environment)
    - [Single step](#single-step)
      - [Application](#application)
      - [Tests](#tests)
  - [Resources](#resources)

## Prepare

If using `vscode` remember to set your interpreter location to `.venv/bin/python`

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run format
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

## pytest

```sh
pipenv run test --help

# show available fixtures
pipenv run test -vvvv --fixtures

pipenv run test -vvvv --no-header

# show print() messages
pipenv run test -vvvv --capture=no
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./31_pytest/.venv/bin/python3.11`

### Pipenv Environment

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

### Single step

#### Application

- Copy the `launch.json` to the root `.vscode`
- `. ./.env` in the terminal

#### Tests

- Configure pytest using the beaker icon in `vscode`
- You can run and debug the discovered tests

## Resources

- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
- pytest: helps you write better programs [here](https://docs.pytest.org/en/stable/)
- https://betterstack.com/community/guides/testing/pytest-guide/
- https://docs.python.org/3/library/sqlite3.html
  https://pytest-with-eric.com/configuration/pytest-stdout/
