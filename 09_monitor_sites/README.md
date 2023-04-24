# MONITORING SITES

Demonstrate a simple tool for testing websites.  

TODO:

* include httpbin compose
* add a despatcher class for the results
* pydoc
* tests
* test behaviour of complex regex

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

# run with arguments
pipenv run start --test
pipenv run start:test 
```

```sh
pipenv run docker:start

# podinfo
curl 0.0.0.0:9001
# httpbin
curl 0.0.0.0:9002

```


## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Created

```sh
# install
pipenv install --dev flake8 flake8-bugbear flake8-2020 black
pipenv install --dev pytest 
pipenv install pyyaml python-json-logger python-dotenv
```

## Resources


