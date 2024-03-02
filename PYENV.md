# PYENV

We use `pyenv` to host multiple versions of python.  

TODO:

* I'm still getting issues with pyenv and it not working correctly on WSL. It seems the APT installed version always gets precedence when shells are invoked by other processes - during node-gyp builds and poetry seems to pick up incorrect versions as well.  

## Contents

- [PYENV](#pyenv)
  - [Contents](#contents)
  - [pyenv](#pyenv-1)
  - [Modify .zshrc](#modify-zshrc)
  - [Troubleshooting failed builds](#troubleshooting-failed-builds)
    - [ERROR:root:code for hash blake2b was not found.](#errorrootcode-for-hash-blake2b-was-not-found)
  - [Resources](#resources)
    - [Issues](#issues)

## pyenv

REF: pyenv [here](https://github.com/pyenv/pyenv)

```sh
# install pyenv version manager
brew install pyenv

# list versions available to install
pyenv install --list

# install a version
pyenv install 3.11.1

# list local versions installed
pyenv versions

# set my global version
pyenv global 3.11.1
```

## Modify .zshrc

```sh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PIPENV_PYTHON="$PYENV_ROOT/shims/python"

plugin=(
  pyenv
)

eval "$(pyenv init -)"
```

## Troubleshooting failed builds

If `pyenv` fails to install a version of python with build errors

NOTE: Follow the steps below to build with TCL and Hashlib working.  

```sh
sudo apt update
sudo apt install \
    build-essential \
    curl \
    libbz2-dev \
    libffi-dev \
    liblzma-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev \
    llvm \
    make \
    tk-dev \
    wget \
    xz-utils \
    zlib1g-dev \
    python-tk \
    python3-tk \
    libb2-1 \
    libb2-dev 
```

You can also `export PYENV_DEBUG=true`  

```sh
brew install tcl-tk

env \   
  PATH="$(brew --prefix tcl-tk)/bin:$PATH" \
  LDFLAGS="-L$(brew --prefix tcl-tk)/lib" \
  CPPFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PKG_CONFIG_PATH="$(brew --prefix tcl-tk)/lib/pkgconfig" \
  CFLAGS="-I$(brew --prefix tcl-tk)/include" \
  PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I$(brew --prefix tcl-tk)/include' --with-tcltk-libs='-L$(brew --prefix tcl-tk)/lib -ltcl8.6 -ltk8.6'" \
  pyenv install 3.11.8
```

Test TCL/TK  

```python
# test 
python

import tkinter
tkinter.TclVersion, tkinter.TkVersion
tkinter._test()
```

### ERROR:root:code for hash blake2b was not found.  

Running `pip list` prints `hash blake2b was not found`.  

To repro simply.  

```python
python

import hashlib
```

I seemed to have fixed this by installing the correct versions of the libb2 libraries.  

```sh
apt list --installed 
brew info openssl
brew unlink openssl
openssl version  #OpenSSL 3.2.1 30 Jan 2024 (Library: OpenSSL 3.2.1 30 Jan 2024)

/usr/bin/openssl version #OpenSSL 3.0.2 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

brew info libb2  #libb2: stable 0.98.1 (bottled)
apt search libb2
sudo apt install libb2-dev
sudo apt install libb2-1     
```

## Resources

* pyenv/pyenv repo [here](https://github.com/pyenv/pyenv)
* Installing pyenv on macOS for Zsh using Homebrew [here](https://gist.github.com/josemarimanio/9e0c177c90dee97808bad163587e80f8)  

### Issues

* import hashlib throwing error on pyenv installation of Arm64 Python 3.11: "unsupported hash type blake2s" [here](https://github.com/pyenv/pyenv/issues/1529)
* ERROR:root:code for hash blake2b was not found in CPython 3.6.7 [here](https://github.com/pyenv/pyenv/issues/1529)
* Unable to install tkinter with pyenv Pythons on MacOS [here](https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos). This also works on WSL.  
