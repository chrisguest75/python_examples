# KAFKA EXAMPLE

Demonstrate a producer consumer with `kafka`  

## Tooling

```sh
brew install aiven-client
avn --help

# authenticate and provide token
avn user login [SSO login email] --token

avn project list

avn service list
SERVICE_NAME="[service]"

avn service topic-list ${SERVICE_NAME}
avn service topic-get ${SERVICE_NAME} default_topic
avn service acl-list ${SERVICE_NAME}
avn service user-list ${SERVICE_NAME}
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

# with topics using admin privleges
pipenv run start --admin --publisher --create --topic my_topic
pipenv run start --admin --consumer --create --topic my_topic

pipenv run start --admin --publisher --topic my_topic2
pipenv run start --admin --consumer --topic my_topic2

# if not using admin the user will need access to the topic
pipenv run start --publisher --topic my_topic2
pipenv run start --consumer --topic my_topic2
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main
```

## Resources

* dpkp/kafka-python repo [here](https://github.com/dpkp/kafka-python/blob/master/example.py)  
* confluentinc/confluent-kafka-python repo [here](https://github.com/confluentinc/confluent-kafka-python)  
* kafka-python documentation [here](https://kafka-python.readthedocs.io/en/master/)  
* Aiven CLI [here](https://docs.aiven.io/docs/tools/cli)  
* Kafka-Python explained in 10 lines of code [here](https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1)  
* Use kcat with Aiven for Apache Kafka® [here](https://docs.aiven.io/docs/products/kafka/howto/kcat)  
