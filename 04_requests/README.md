# REQUESTS

Demonstrate examples of using `requests` package  

## 🏠 Start

```sh
# start with overrides and shared port (this will not work)
docker compose up -d

# quick test
curl 0.0.0.0:9001
```

## Run

```sh
pipenv run test

pipenv run start --simple --url http://0.0.0.0:9001
```

## 🧼 Cleanup

```sh
# bring it down and delete the volume
docker compose down --volumes
```

## 👀 Resources

* stefanprodan/podinfo [here](https://github.com/stefanprodan/podinfo)  

https://pypi.org/project/requests-mock/