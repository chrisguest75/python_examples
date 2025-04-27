# MIDI

Generate midi events.  

TODO:

* Save a midi file https://dev.to/dm8ry/automating-midi-generation-with-python-a-comprehensive-guide-ckb
* Create a simple arpeggio

## Contents

- [MIDI](#midi)
  - [Contents](#contents)
  - [Dependencies](#dependencies)
  - [Install](#install)
  - [Start](#start)
  - [Created](#created)
  - [Resources](#resources)

## Dependencies

* tmuxinator

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

* A Python binding for the RtMidi C++ library implemented using Cython. [here](https://github.com/SpotlightKid/python-rtmidi)
* python-rtmidi docs [here](https://spotlightkid.github.io/python-rtmidi/)
* A set of C++ classes that provide a common API for realtime MIDI input/output across Linux (ALSA & JACK), Macintosh OS X (CoreMIDI & JACK), Windows (Multimedia Library & UWP), Web MIDI, iOS and Android. [here](https://github.com/thestk/rtmidi)
* examples [here](https://github.com/SpotlightKid/python-rtmidi/tree/master/examples)
