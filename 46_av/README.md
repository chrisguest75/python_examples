# AV MEDIA HANDLING

Demonstrate using `av` library.

NOTES:

- Pillow library needs to be installed.

## Contents

- [AV MEDIA HANDLING](#av-media-handling)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Generate Media](#generate-media)
    - [Video](#video)
  - [Audio](#audio)
  - [Local](#local)
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
# required in terminal if using pipenv
# for vscode
export PIPENV_IGNORE_VIRTUALENVS=1
export PIPENV_VENV_IN_PROJECT=1

# install
pipenv install --dev
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
pipenv run start
```

## Generate Media

### Video

```sh
## No audio, No keyframes
mkdir -p ./out/testcard/
mkdir -p ./out/frames/

# testcard without audio (20 seconds)
ffmpeg -f lavfi -i testsrc=size=960x720 -t 5 -r 30 -pix_fmt yuv420p -vf "drawtext=fontfile=/windows/fonts/arial.ttf:text='Testcard':fontcolor=white:fontsize=100" -force_key_frames 00:00:00.000 -b_strategy 0 -sc_threshold 0 ./out/testcard/testcard_960_720p_30fps.mp4
```

## Audio

```sh
mkdir -p ./out/audio/
# get rss feed
curl -s -o ./out/audio/lnlrss.xml https://latenightlinux.com/feed/mp3
# get first url
FEED_URL=$(xmllint --xpath 'string(//rss/channel/item[1]/enclosure/@url)' --format --pretty 2 ./out/audio/lnlrss.xml)
# get the file
PODCASTFILE=$(basename $FEED_URL)
curl -s -L -o ./out/audio/${PODCASTFILE} $FEED_URL
```

## Local

```sh
# start - will also build
just start_frames write_frames
just start_audio audio_speedup
just start_hls export_hls_audio

vlc ./out/audio_speedup.wav
```

## Docker

```sh
# start - will also build
just start_image slim

# print out size and labels
just details slim

# look at contents
just dive slim
```

## Debugging and Troubleshooting

### Interpreter

Set the interpreter path to `./46_av/.venv/bin/python3.11`

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
- PyAV Documentation [here](https://pyav.basswood-io.com/docs/stable/)  
  https://stackoverflow.com/questions/2677317/how-to-read-remote-video-on-amazon-s3-using-ffmpeg
