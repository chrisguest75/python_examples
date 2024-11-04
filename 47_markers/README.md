# MARKERS

Print out the markers used by different versions of python controlled in the `.python_version`.  

## Start

```sh
# install
# CPYTHON
pyenv local 3.10.9
python --version
just clean
just install
just start

# pypy
pyenv install pypy3.10-7.3.15
pyenv local pypy3.10-7.3.15
python --version
just clean
just install
just start
```

## Resources

* PEP 496 – Environment Markers [here](https://peps.python.org/pep-0496/)
