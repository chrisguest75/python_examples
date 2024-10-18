# pypy

Demonstrate using pypy to run with a docker container.  

## Contents

- [pypy](#pypy)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
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
pyenv install pypy3.10-7.3.17
# write .python-version
pyenv local pypy3.10-7.3.17
pyenv which python

export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev --python=$(pyenv which python)

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

## Docker

```sh
pipenv run docker:build
# or
pipenv run docker:build:pypy       
pipenv run docker:start   

# troubleshooting    
docker run -it --entrypoint /bin/bash 37_pypy
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./37_pypy/.venv/bin/python3.11`

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
