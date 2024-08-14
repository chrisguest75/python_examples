# 32_pdoc

Demonstrate `pdoc` tool for generating documentation from docstrings.  

## Contents

- [32\_pdoc](#32_pdoc)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Build docs](#build-docs)
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

## Build docs

```sh
# build docs
pipenv run docs

# render them
pipenv run docs:serve
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./32_pdoc/.venv/bin/python3.11`

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
- pdoc repo [here](https://github.com/mitmproxy/pdoc/tree/main)