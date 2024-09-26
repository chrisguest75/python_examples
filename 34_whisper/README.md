# Whisper

Demonstrate whisper build and tracing with OTEL

## Contents

- [Whisper](#whisper)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Just](#just)
  - [Configuration](#configuration)
  - [Audio](#audio)
  - [Debugging and Troubleshooting](#debugging-and-troubleshooting)
    - [Container](#container)
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

## Just

```sh
# terminal 1
just collector-restart
# you can check collector metrics here.
curl 0.0.0.0:8888/metrics

# terminal 2
just service-run
```

## Configuration

```sh
pipenv  install opentelemetry-distro
pipenv run -- opentelemetry-bootstrap -a install


pipenv run -- opentelemetry-instrument --help
pipenv run -- opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console --service_name 34_whisper --disabled_instrumentations aws-lambda --log_level TRACE python main.py --test

pipenv run -- opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console --service_name 34_whisper --log_level TRACE python main.py --test
```

## Audio

```sh
mkdir -p ./sources
# get rss feed
curl -s -o ./sources/lnlrss.xml https://latenightlinux.com/feed/mp3
# get first url
FEED_URL=$(xmllint --xpath 'string(//rss/channel/item[1]/enclosure/@url)' --format --pretty 2 ./sources/lnlrss.xml)
# get the file
PODCASTFILE=$(basename $FEED_URL)
curl -s -L -o ./sources/${PODCASTFILE} $FEED_URL
```

## Debugging and Troubleshooting

### Container

```sh
dive 34_whisper:latest

docker exec -it 34_whisper /bin/bash
```

### Interpreter

Set the interpreter path to `./34_whisper/.venv/bin/python3.11`

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
- https://pypi.org/project/numpy/
- https://christophergs.com/blog/ai-podcast-transcription-whisper
- https://opentelemetry.io/docs/languages/python/
- https://opentelemetry.io/docs/languages/python/getting-started/
