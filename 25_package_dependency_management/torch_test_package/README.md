# TORCH TEST PACKAGE

A package that imports `pytorch` cpu.

## Build

```sh
# install packages
pipenv install --dev
# run build 
pipenv run build
```

## Created

```sh
export PIPENV_VENV_IN_PROJECT=1
pipenv --python 3.11.9 install

pipenv install --dev pytest build twine

# NOT WORKING
#[[source]]
#url = "https://download.pytorch.org/whl/cpu"
#verify_ssl = true
#name = "pytorch"
pipenv install --index pytorch pytorch 

# quick test
pipenv run python src/torch_test_package/main.py
```

## Resources

* Configuring setuptools using pyproject.toml files [here](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
* PyTorch GET STARTED [here](https://pytorch.org/get-started/locally/#windows-package-manager)
* A Gentle Introduction to PyTorch for Beginners (2023) [here](https://www.dataquest.io/blog/pytorch-for-beginners/)
* Specifying Package Indexes [here](https://github.com/pypa/pipenv/blob/main/docs/indexes.md)
* Packaging Python Projects [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* Pipenv Installation [here](https://pipenv.pypa.io/en/latest/installation.html)
* PEP 631 – Dependency specification in pyproject.toml based on PEP 508 [here](https://peps.python.org/pep-0631/)
* pyproject.toml [here](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
