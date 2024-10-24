# 41_pyspy

Demonstrate how to use `pyspy`

TODO:

- Trace native code
- Create a more complicated example
- pypy versus cpython

## Contents

- [41_pyspy](#41_pyspy)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Profiling](#profiling)
  - [Docker](#docker)
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
export PIPENV_IGNORE_VIRTUALENVS=1
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

## Profiling

```sh
# create output folder
mkdir -p ./out

# pyspy (requires sudo for sampling)
sudo pipenv run pyspy
```

## Docker

```sh
pipenv run docker:build
pipenv run docker:start

# troubleshooting
docker run -it --entrypoint /bin/bash 41_pyspy
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./41_pyspy/.venv/bin/python3.11`

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
- https://github.com/benfred/py-spy
