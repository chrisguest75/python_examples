# 34_whisper

Demonstrate 34_whisper

## Contents

GENERATE CONTENTS HERE

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
