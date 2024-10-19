# GITPYTHON

Demonstrate `gitpython`

## Contents

- [GITPYTHON](#gitpython)
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
pipenv run start --path ../
pipenv run start:test
```

## Docker

```sh
pipenv run docker:build
pipenv run docker:start
# override path
pipenv run docker:start ./start.sh --path ../

# troubleshooting
docker run -it --entrypoint /bin/bash 40_gitpython
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./40_gitpython/.venv/bin/python3.11`

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

- https://gitpython.readthedocs.io/en/stable/intro.html#api-reference
- https://github.com/PyGithub/PyGithub
- https://github.com/PyGithub/PyGithub/issues/3031
- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
