# CURSES RENDER GAME OF LIFE

Demonstrate importing a package from a different folder in the repository.  

REF: Cells are copied from [chrisguest75/github-of-life](https://github.com/chrisguest75/github-of-life)  

## Install

```sh
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev
```

## Start

```sh
# print help
pipenv run start

# list all the cell files
pipenv run start --list 

# show info on a cell file
pipenv run start --info --file puffer2.cells

# use a cell flle and play game of life
pipenv run start --file puffer2.cells

> press q to exit
```

## Resources

* [chrisguest75/github-of-life](https://github.com/chrisguest75/github-of-life)  
