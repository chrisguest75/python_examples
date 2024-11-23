# README

A repository containing python examples.

## Conventional Commits

NOTE: This repo has switched to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0). It requires `pre-commit` and `commitizen` to help with controlling this.

```sh
# install pre-commmit (prerequisite for commitizen)
brew install pre-commit
brew install commitizen
# conventional commits extension
code --install-extension vivaxy.vscode-conventional-commits

# install hooks
pre-commit install --hook-type commit-msg --hook-type pre-push
```

## VSCODE

- If using vscode if you `pipenv --rm` it might be best to reload
- Select the interpreter to get black code formatting. On a mac use `cmd + shift + .` in the folder select dialog or set path to `.venv/bin/python`  
- Running tests can be done by selecting `Testing` extension
- To get the formatting on save you need to open in the project folder

## Devcontainers

### Python 3.11

[.devcontainer/python_3_11/README.md](./.devcontainer/python_3_11/README.md)

## Configuration

### pyenv

We use pyenv to host multiple versions of python.  
Help configuring it REF: [PYENV.md](./PYENV.md).

## pipenv

REF: Pipenv: Python Dev Workflow for Humans [here](https://pipenv.pypa.io/en/latest/)

Pipenv does not recommend installing using `brew`. Instead use the package.  

```sh
python -m site    
pip install pipenv --user     
export PATH=${HOME}/.local/bin:$PATH
pipenv
```

### Configuring and running

```sh
# required if you're already in a virtualenv.
export PIPENV_IGNORE_VIRTUALENVS=1
# keep venv in folder (this is my preference - need to reevalute it)
export PIPENV_VENV_IN_PROJECT=1

cd xx_my_project

# create a new project in current folder.
pipenv install

# check installed packages
pipenv run pip list

# enter venv
pipenv shell

# installing packages
pipenv install --dev flake8

# remove venv if you want to
pipenv --rm
```

### Troubleshooting

If your pip.conf gets overwritten.

```sh
# pip input-url
cat $HOME/.config/pip/pip.conf

> [global]
> index-url = https://pypi.org/simple
```

Clean down system pip after installing global packages.

```sh
pip3 list

pip3 freeze > ./requirements.txt

pip3 uninstall -r ./requirements.txt --yes
```

### Maintaining

Goto [UPGRADING.md](./UPGRADING.md)

## Resources

- pyenv [here](https://github.com/pyenv/pyenv)
- What’s New In Python 3.11 [here](https://docs.python.org/3/whatsnew/3.11.html)
- Pipenv: Python Dev Workflow for Humans [here](https://pipenv.pypa.io/en/latest/)
