# PIPX

pipx — Install and Run Python Applications in Isolated Environments

NOTES:

- Not sure how this works with mulitple `pyenv` versions.

## Install PipX

Preferential to have `pipx` installed for each version.

```sh
pip install pipx

# this will add paths
pipx ensurepath
echo $path
```

## Install Package

```sh
pipx install pycowsay

which pycowsay

pycowsay "hello"
```

## Resources

- pipx — Install and Run Python Applications in Isolated Environments [here](https://pipx.pypa.io/stable/)
- pypa/pipx repo [here](https://github.com/pypa/pipx)
- Using Different Versions Of Python With Pipx | Pyenv [here](https://waylonwalker.com/pyenv-pipx/)
