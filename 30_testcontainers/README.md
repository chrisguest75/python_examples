# 30_testcontainers

Demonstrate 30_testcontainers

TODO:

- This is not working yet. Getting a failure running tests AttributeError: 'PostgresContainer' object has no attribute 'POSTGRES_USER'

## Contents

- [30_testcontainers](#30_testcontainers)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
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
#
pipenv install "psycopg[binary,pool]" "testcontainers[postgres]"
```

## Resources

- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
- What is Testcontainers? [here](https://testcontainers.com/getting-started/)
- https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/
  https://testcontainers-python.readthedocs.io/en/latest/
- testcontainers/testcontainers-python repo [here](https://github.com/testcontainers/testcontainers-python)
