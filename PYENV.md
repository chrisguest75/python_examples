# PYENV

Using pyenv to control versions.  

TODO:

* I'm still getting issues with pyenv and it not working correctly on WSL. It seems the APT installed version always gets precedence when shells are invoked by other processes - during node-gyp builds and poetry seems to pick up incorrect versions as well.  

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

## Resources

* Installing pyenv on macOS for Zsh using Homebrew [here](https://gist.github.com/josemarimanio/9e0c177c90dee97808bad163587e80f8)  
