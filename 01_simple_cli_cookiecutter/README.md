# CLI COOKIECUTTTER

A cli cookiecutter for quickly spinning up new projects.

TODO:

* Add a dockerfile (multistage linting,running tests, etc)
* Add pdoc

## Contains

* Pipenv
* Logging
* Linting
* Argument parsing
* Pytest

## Install

```sh
brew install cookiecutter

cookiecutter --help
cookiecutter --version
```

## Usage

```sh
# in root
cd $(git root)

# it will create directory of project name
cookiecutter $(pwd)/01_simple_cli_cookiecutter
```

## Resources

- cookiecutter/cookiecutter [here](https://github.com/cookiecutter/cookiecutter)
- cookiecutter installation [here](https://cookiecutter.readthedocs.io/en/stable/installation.html)
- cookiecutter/cookiecutter-django [here](https://github.com/cookiecutter/cookiecutter-django/tree/master)
