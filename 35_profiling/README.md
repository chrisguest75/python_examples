# Profiling

Demonstrate profiling tools  

## Contents

- [Profiling](#profiling)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Profiling](#profiling-1)
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

## Profiling

```sh
# install dot
sudo apt install graphviz
```

```sh
# profiling 
pipenv run profile --test
# save out stats
pipenv run profile:save --test

pipenv run profile:dot
pipenv run profile:render
```


## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./35_profiling/.venv/bin/python3.11`

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


https://medium.com/@narenandu/profiling-and-visualization-tools-in-python-89a46f578989
- Python testing in Visual Studio Code [here](https://code.visualstudio.com/docs/python/testing#_example-test-walkthroughs)
