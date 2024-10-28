# TEST CTRANSLATE

Test custom ctranslate2 build

NOTES:

- Follow the instructions to switch between `cpython` and `pypy`

## Contents

- [TEST CTRANSLATE](#test-ctranslate)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Process model](#process-model)
  - [Builds](#builds)
    - [CPYTHON](#cpython)
    - [PYPY](#pypy)
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
# for vscode
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

## Process model

```sh
# process the model
just model
```

## Builds

### CPYTHON

```sh
# CPYTHON
pyenv local 3.11.9
python --version
just clean 

# install cypthon locally
just REQUIREMENTS_CATEGORY="dev-packages packages cpython" install

# CPYTHON local
just start_local

# works
just BASE_IMAGE="python:3.10.15-slim-bookworm" REQUIREMENTS_CATEGORY="packages cpython" start
```

### PYPY

```sh
# pypy
pyenv local pypy3.10-7.3.17
python --version
just clean 

just REQUIREMENTS_CATEGORY="dev-packages packages pypy" install

# pypy local 
just start_local

# pypy docker 
just BASE_IMAGE="pypy:3.10-7.3.17-bookworm" REQUIREMENTS_CATEGORY="packages pypy" start

# add no-cache
just DOCKER_BUILD_ARGUMENTS="--no-cache" REQUIREMENTS_CATEGORY="packages pypy" start
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./test_ctranslate2/.venv/bin/python3.11`

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
- SentencePiece is an unsupervised text tokenizer and detokenizer [here](https://github.com/google/sentencepiece)
