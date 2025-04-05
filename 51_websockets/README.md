# WEBSOCKETS

Demonstrate `websockets` by using AV to decode an MP3 as PCM and send it over a websocket for saving in a WAV file.  

TODO:

* producer consumer example
* wrapping binary data in a structure
* aysncio queue

## Contents

- [WEBSOCKETS](#websockets)
  - [Contents](#contents)
  - [Install](#install)
  - [Start](#start)
  - [Created](#created)
  - [Resources](#resources)

## Install

```sh
just nix
```

## Start

```sh
just lint

just format

just test

just start-server --server

just start-client --client --file audio/english_thelittlegraylamb_sullivan_csm_64kb.mp3

vlc ./recording/recorded_audio.wav
```

## Created

When installing a fresh UV project.  

```sh
# create a basic skeleton
uv init .

# add packages
uv add pyyaml

# add dev 
uv add --dev flake8-2020 
```

## Resources

* https://websockets.readthedocs.io/en/stable/intro/index.html
* An extremely fast Python package and project manager, written in Rust. [here](https://docs.astral.sh/uv/)
* https://github.com/astral-sh/uv
* https://www.datacamp.com/tutorial/python-uv
