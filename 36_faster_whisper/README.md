# FASTER WHISPER

Demonstrate faster_whisper

## Contents

- [FASTER WHISPER](#faster-whisper)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Docker](#docker)
  - [Audio](#audio)
  - [Profiling](#profiling)
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

## Docker

```sh
pipenv run docker:build       

mkdir -p ./.model-cache

pipenv run docker:start   
# share volume into profile  
pipenv run docker:profile

# troubleshooting    
docker run -it --entrypoint /bin/bash 36_faster_whisper
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

# trim and skip music
ffmpeg -hide_banner -i ./sources/${PODCASTFILE} -ss 00:02:00 -t 00:01:00 ./sources/LNL301_1mins.mp3
/mnt/c/Program\ Files/VideoLAN/VLC/vlc.exe ./sources/LNL301_1mins.mp3 
```

## Profiling

```sh
# install dot
sudo apt install graphviz
```

```sh
mkdir -p ./out

# profiling 
pipenv run profile --test
# save out stats
pipenv run profile:save --test

pipenv run profile:dot
pipenv run profile:render
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./36_faster_whisper/.venv/bin/python3.11`

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
