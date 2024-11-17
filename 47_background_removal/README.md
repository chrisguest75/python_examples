# BACKGROUND REMOVAL

Background removal and conversion to SVG example.

TODO:

- Try to do in one svg object with animation https://gsap.com/

## Contents

- [BACKGROUND REMOVAL](#background-removal)
  - [Contents](#contents)
  - [Prepare](#prepare)
  - [Start](#start)
  - [Local](#local)
  - [Download Content](#download-content)
  - [Remove Background](#remove-background)
  - [SVG Outlines](#svg-outlines)
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
pipenv run start --test
pipenv run start:test
```

## Local

```sh
# start - will also build
just start
```

## Download Content

```sh
mkdir -p ./out
VIDEO_URL=https://www.youtube.com/shorts/56Mrl-QIGE4
VIDEO_URL=https://www.youtube.com/shorts/jMOoVUPyLPQ

yt-dlp -o ./out/dance.mp4 $VIDEO_URL

vlc ./out/dance.mp4.webm

mkdir -p ./out/frames

# exports
ffmpeg -i ./out/dance.mp4.webm ./out/frames/dance_%05d.jpg
export START_TIME=00:00:00
export DURATION=00:30
ffmpeg -i ./out/dance.mp4.webm -ss ${START_TIME} -t ${DURATION} ./out/frames/dance_%05d.jpg
```

## Remove Background

```sh
#pipenv run start:test --convert background --input ./out/frames/dance_00001.jpg --output ./out/converted/dance_00001.png

# convert a directory
pipenv run start:test --convert background --input ./out/frames --output ./out/converted

# mkdir -p ./out/convertedbmp
# mkdir -p ./out/svg

# for file in ./out/converted/dance_*.png; do
#     # remove extension
#     outname="${file%.*}"
#     bmppath="./out/convertedbmp/$(basename $outname).bmp"
#     svgpath="./out/svg/$(basename $outname).svg"
#     convert "$file" "$bmppath"
#     potrace --svg --output "$svgpath" "$bmppath"
# done

# export NUMBER=00010
# convert "./out/converted/dance_${NUMBER}.png" ./out/convertedbmp/dance_${NUMBER}.bmp
# potrace --svg --output ./out/svg/dance_${NUMBER}.svg ./out/convertedbmp/dance_${NUMBER}.bmp

# # open in chrome
# open ./out/svg/dance_${NUMBER}.svg
```

## SVG Outlines

Once you have the `frames.json` start in liveserver extension to view.

```sh
# convert removed backgrounds to svg
pipenv run start:test --convert mask --input ./out/converted --output ./out/mask

# convert a directory of masks to svg
pipenv run start:test --convert svg --input ./out/mask --output ./out/svgmask
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

Set the interpreter path to `./47_background_removal/.venv/bin/python3.11`

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
