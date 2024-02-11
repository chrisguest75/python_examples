# TARBALL

Demonstrate a simple tarball tool to index and extract from large files.

REF: [shell_examples/73_creating_archives/TAR.md](https://github.com/chrisguest75/shell_examples/blob/master/73_creating_archives/TAR.md)

## Create example TAR

```sh
mkdir -p ./out

# dereference is following symbolic links
tar -cvf ./out/test.tar  --dereference .
```

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run lint
pipenv run test

# enter venv
pipenv shell

# create .env file
cp .env.template .env

# run with arguments
pipenv run start --info --file ./out/test.tar
pipenv run start:info
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

- https://www.gnu.org/software/tar/manual/html_node/Standard.html
- https://docs.fileformat.com/compression/tar/
- https://en.wikipedia.org/wiki/Tar_(computing)
