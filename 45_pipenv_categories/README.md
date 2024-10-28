# PIPENV CATEGORIES

Demonstrate `pipenv` categories.

NOTES:

- You can use `pipenv` categories to switch packages that get installed.
- BE CAREFUL: You have to rebuild the `Pipfile.lock` as it is this that determines the packages to be used.
- BE CAREFUL: You should be exporting the hashes into the requirements file. Otherwise when installing the GPU category it would get very confused installing the nvidia libs but `pytorch+cpu` package  

TODO:

- Test if you can use it to override packages to instead install a local build.

## Contents

- [PIPENV CATEGORIES](#pipenv-categories)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Local](#local)
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
# required in terminal if using pipenv
# for vscode
export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VENV_IN_PROJECT=1

# install
pipenv install --dev
just install

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

## Local

```sh
just lock

# output the requirements.txt
just REQUIREMENTS_CATEGORY="dev-packages" requirements
just REQUIREMENTS_CATEGORY="packages cpu" requirements

# look at packages listed in output (switch cpu to gpu in the justfile REQUIREMENTS_CATEGORY)
just REQUIREMENTS_CATEGORY="dev-packages cpu version-pypy version-cpython" start_image slim

# --no-cache
just DOCKER_BUILD_ARGUMENTS="--no-cache" REQUIREMENTS_CATEGORY="dev-packages cpu version-pypy version-cpython" start_image slim

# gpu
just REQUIREMENTS_CATEGORY="dev-packages gpu version-pypy version-cpython" start_image slim
```

## Docker

```sh
# start - will also build
just start_image slim

# print out size and labels
just details slim

# look at contents
just dive slim
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./45_pipenv_categories/.venv/bin/python3.11`

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
