# FAKER

Demonstrate a data faker testbed.

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
pipenv run start --generate
pipenv run start:generate
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

* Faker documentation [here](https://faker.readthedocs.io/en/master/fakerclass.html)  
* joke2k/faker [here](https://github.com/joke2k/faker)