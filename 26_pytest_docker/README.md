# PYTEST DOCKER

Demonstrate pytest docker and how it allows containers to be started within tests.  

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
pipenv run start --test
pipenv run start:test
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

* https://pypi.org/project/pytest-docker/
* https://httpbin.org/
* https://github.com/avast/pytest-docker