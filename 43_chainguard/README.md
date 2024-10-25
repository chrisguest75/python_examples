Use chainguard to build images.  

REF: Dockerexamples

TODO:

* Use pipenv to install

NOTES:

* Distroless images
* Use the `-dev` images to include shell `/bin/sh`

## Contents

GENERATE CONTENTS HERE

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

## Build

```sh
just build
docker build -f Dockerfile.chainguard . -t octo-facts

docker run --rm octo-facts

docker run -it --rm --entrypoint /bin/sh octo-facts
```

## Docker

```sh
pipenv run docker:build       
pipenv run docker:start   

# troubleshooting    
docker run -it --entrypoint /bin/bash 43_chainguard
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

* Copy the `launch.json` to the root `.vscode`
* `. ./.env` in the terminal

#### Tests

* Configure pytest using the beaker icon in `vscode`
* You can run and debug the discovered tests

## Resources

* Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
* <https://edu.chainguard.dev/chainguard/chainguard-images/getting-started/python/>
* <https://edu.chainguard.dev/chainguard/chainguard-images/how-to-use-chainguard-images/>
