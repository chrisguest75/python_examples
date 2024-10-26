# CHAINGUARD

Use chainguard to build images.

REF: [github.com/chrisguest75/docker_examples/A0_chainguard/README.md](https://github.com/chrisguest75/docker_examples/blob/master/A0_chainguard/README.md)

NOTES:

- Distroless images
- Use the `-dev` images to include shell `/bin/sh`
- The image is 50% smaller.

## Contents

- [CHAINGUARD](#chainguard)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Build \& Run](#build--run)
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

## Build & Run

```sh
just start

just start_chainguard
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./43_chainguard/.venv/bin/python3.11`

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
- Getting Started with the Python Chainguard Image [here](https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/)
- How to Use Chainguard Images [here](https://edu.chainguard.dev/chainguard/chainguard-images/how-to-use-chainguard-images/)
