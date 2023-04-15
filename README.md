# README

A repo containing some python examples.  

TODO:

* a simple cli
* pytest/pymock
* using requests library
* pandas
* dockerising
* debugging
* quokka style environment
* OTEL

## Configuration

REF: pyenv [here](https://github.com/pyenv/pyenv)  

### pyenv

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

## pipenv

REF: Pipenv: Python Dev Workflow for Humans [here](https://pipenv.pypa.io/en/latest/)  
 
```sh
# required if you're already in a virtualenv.
export PIPENV_IGNORE_VIRTUALENVS=1 
# keep venv in folder (this is my preference - need to reevalute it)
export PIPENV_VENV_IN_PROJECT=1

cd xx_my_project

# create a new project in current folder.
pipenv install

# remove venv if you want to
pipenv --rm
```

## Resources

* pyenv [here](https://github.com/pyenv/pyenv)  
* What’s New In Python 3.11 [here](https://docs.python.org/3/whatsnew/3.11.html)  
* Pipenv: Python Dev Workflow for Humans [here](https://pipenv.pypa.io/en/latest/)  
