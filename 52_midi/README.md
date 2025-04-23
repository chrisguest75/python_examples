# MIDI

Generate midi events.  

TODO:

* Generate midi events onto channel
* Save a midi file
* Create a simple arpeggio

## Contents

- [MIDI](#midi)
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

just start --test
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

* https://github.com/SpotlightKid/python-rtmidi
* https://spotlightkid.github.io/python-rtmidi/
* https://github.com/thestk/rtmidi
* https://github.com/SpotlightKid/python-rtmidi/tree/master/examples
* An extremely fast Python package and project manager, written in Rust. [here](https://docs.astral.sh/uv/)
* https://github.com/astral-sh/uv
* https://www.datacamp.com/tutorial/python-uv
