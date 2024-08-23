# PYTEST

Demonstrate `pytest` features.

REF: [github.com/chrisguest75/py_coverage_example/README.md](https://github.com/chrisguest75/py_coverage_example/blob/master/README.md)

TODO:

- Finish off the dockerfile to remove dev packages in another stage
- pytest --fixtures
- pymock
- coverage

## Contents

- [PYTEST](#pytest)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [pytest](#pytest-1)
  - [coverage](#coverage)
  - [docker build](#docker-build)
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

Pytest specifics.

```sh
# show options
pipenv run test --help

# show available fixtures
pipenv run test -vvvv --fixtures

# breaks down into individual tests
pipenv run test -vvvv --no-header

# show print() messages
pipenv run test -vvvv --capture=no

# run a single file
pipenv run test tests/test_bubble_sort.py
```

## coverage

```sh
# create coverage report
pipenv run test:coverage

# serve up the coverage report
pipenv run test:serve
```

## docker build

The docker build will run `flake8` linting, `pytest` and `pipenv check`  

```sh
# build and run the container
pipenv run docker:build && pipenv run docker:run 
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
