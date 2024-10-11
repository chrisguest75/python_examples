# FASTER WHISPER

Demonstrate faster_whisper

Ref: [docker_examples/A2_gpu](https://github.com/chrisguest75/shell_examples/tree/master/A2_gpu)  
Ref: [shell_examples/81_gpu](https://github.com/chrisguest75/shell_examples/tree/master/81_gpu)  

TODO:

* Get cuda working https://medium.com/@albertqueralto/enabling-cuda-capabilities-in-docker-containers-51a3566ad014

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
# in vscode terminal
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

## Docker

Build either `gpu|cpu`  

```sh
pipenv run docker:build:gpu|cpu      

mkdir -p ./.model-cache

pipenv run docker:start:gpu|cpu     
# share volume into profile  
pipenv run docker:profile:gpu|cpu     

# gui
pipenv run profile:snakeviz:gpu|cpu     

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

Local  

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

# gui
pipenv run profile:snakeviz:gpu|cpu
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
- CUDA Toolkit 12.6 Update 2 Downloads [here](https://developer.nvidia.com/cuda-downloads)
- Installing cuDNN on Linux [here](https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html)
- CUDA and cuDNN images from gitlab.com/nvidia/cuda [here](https://hub.docker.com/r/nvidia/cuda/)
- https://github.com/SYSTRAN/faster-whisper/issues/516
