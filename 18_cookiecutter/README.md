# COOKIECUTTTER

Demonstrate how to use `cookiecutter`.

## Install

```sh
brew install cookiecutter

cookiecutter --help
cookiecutter --version
```

## Create Zip

```sh
rm -rf ./out
mkdir -p ./out

zip -r ./out/cookiecutter.zip ./cookiecutter_example

unzip -l ./out/cookiecutter.zip
```

## Cookiecutter

```sh
mkdir -p ./cookiecutter_test

cd ./cookiecutter_test

cookiecutter $(pwd)/../out/cookiecutter.zip
```

## Resources

- cookiecutter/cookiecutter [here](https://github.com/cookiecutter/cookiecutter)
- cookiecutter installation [here](https://cookiecutter.readthedocs.io/en/stable/installation.html)
- cookiecutter/cookiecutter-django [here](https://github.com/cookiecutter/cookiecutter-django/tree/master)
