# test_ctranslate2

Demonstrate test_ctranslate2

NOTES:

* To switch over to pypy
* For pypy the model needs to be downloaded first outside the container. openmnt is not included and it needs torch.  
* `just clean`
* Switch the lib to the locally built one in pipfile
* Set pyenv python version pypy3.10-7.3.17
* `just install` to generate new lock file.
* `just start_pypy`

## Contents

- [test\_ctranslate2](#test_ctranslate2)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Building](#building)
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

## Building

```sh
curl -o model/transformer-ende-wmt-pyOnmt.tar.gz https://s3.amazonaws.com/opennmt-models/transformer-ende-wmt-pyOnmt.tar.gz
tar xf transformer-ende-wmt-pyOnmt.tar.gz

pipenv run ct2-opennmt-py-converter --model_path ./model/averaged-10-epoch.pt --output_dir ./model/ende_ctranslate2
```

## Docker

```sh
pipenv run docker:build       
pipenv run docker:start   

# troubleshooting    
docker run -it --entrypoint /bin/bash test_ctranslate2
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
