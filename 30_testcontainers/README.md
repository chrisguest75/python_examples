# 30_testcontainers

Demonstrate 30_testcontainers

TODO:

- The tests are not working yet.
- Setups are being called twice - do some tests examples.

## Contents

- [30_testcontainers](#30_testcontainers)
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
  - [Packages](#packages)
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

REF: [31_pytest/README.md](../31_pytest/README.md)

```sh
# show options
pipenv run test --help

# breaks down into individual tests
pipenv run test -vvvv --no-header --capture=no tests/test_customers.py
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./30_testcontainers/.venv/bin/python3.11`

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

## Packages

```sh
# install packages
pipenv install "psycopg[binary,pool]" "testcontainers[postgres]"
```

## Resources

- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
- What is Testcontainers? [here](https://testcontainers.com/getting-started/)
- Getting started with Testcontainers for Python [here](https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/)
- testcontainers-python facilitates the use of Docker containers for functional and integration testing [here](https://testcontainers-python.readthedocs.io/en/latest/)
- testcontainers/testcontainers-python repo [here](https://github.com/testcontainers/testcontainers-python)
