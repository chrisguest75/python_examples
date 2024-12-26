# {{ cookiecutter.project_name }}

Demonstrate {{ cookiecutter.project_name }}

## Contents

GENERATE CONTENTS HERE

## Prepare

If using `vscode` remember to set your interpreter location to `.venv/bin/python`

## Start

## Linux/Mac/WSL

```sh
# install
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

## NixOS

Open a pure shell and install packages.  
NOTE: Make sure the `flake.nix` and `flake.lock` are staged in `git`.  

NOTE:

* `numpy` installs precompiled binaries that link to glib expecting FHS compliant filesystem. We have to use `nix-ld` to map the paths from `nix-store`.  
* We map `NIX_LD_LIBRARY_PATH` to `LD_LIBRARY_PATH` - enable this in the justfile.  

```sh
nix develop --impure --command bash -c 'python --version'

# enter the flake - we have to use impure for nix-ld
nix develop --impure

zsh

just install

# create .env file
cp .env.template .env

just start
```

## Local

```sh
# start - will also build
just start
```

{% if cookiecutter.create_dockerfile == 'y' %}

## Docker

```sh
# start - will also build
just start_image slim

# print out size and labels
just details slim

# look at contents
just dive slim
```

{% endif %}

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./{{ cookiecutter.project_name }}/.venv/bin/python3.11`

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
