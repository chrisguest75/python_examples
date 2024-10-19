# TEXTUAL

Demonstrate `textual` tui

TODO:

- Change logging over to file logging
- Add an overlay that allows git status to be run on each directory

## Contents

- [TEXTUAL](#textual)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Examples](#examples)
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
pipenv run start --test
pipenv run start:test
```

## Examples

```sh
pipenv run python -m textual
```

## Docker

```sh
pipenv run docker:build
pipenv run docker:start

# troubleshooting
docker run -it --entrypoint /bin/bash 39_textual_tui
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./39_textual_tui/.venv/bin/python3.11`

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

- https://textual.textualize.io/getting_started/#demo
- https://github.com/Textualize/textual
- https://dev.to/wiseai/textual-the-definitive-guide-part-1-1i0p
- https://github.com/juftin/textual-universal-directorytree
- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
