# TEST CTRANSLATE

Test custom ctranslate2 build

NOTES:

- For pypy the model needs to be downloaded first outside the container. openmnt is not included and it needs torch.
- To switch over to pypy
- Run `just clean`
- Switch the lib to the locally built one in pipfile
- Set python version pypy3.10-7.3.17 in the justfile
- Run `just start`

## Contents

- [TEST CTRANSLATE](#test-ctranslate)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Process model](#process-model)
  - [Builds](#builds)
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
just model_download

# needs opennmt-py package installed
pipenv run ct2-opennmt-py-converter --model_path ./model/averaged-10-epoch.pt --output_dir ./model/ende_ctranslate2
```

## Builds

```sh
just start
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
