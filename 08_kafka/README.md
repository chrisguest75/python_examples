# KAFKA EXAMPLE

Demonstrate a producer consumer with `kafka`  

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
pipenv run start --publisher

pipenv run start --consumer
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

```

## Resources

* https://github.com/confluentinc/confluent-kafka-python
* https://kafka-python.readthedocs.io/en/master/
