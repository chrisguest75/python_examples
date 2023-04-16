# SIMPLE FLASK WITH OPENAPI/SWAGGER

Demonstrate a simple flask app that can be used as basis for other apps.  

REF: [chrisguest75/banner_service](https://github.com/chrisguest75/banner_service)  

## Install

```sh
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev
```

## Start

```sh
pipenv run start
```

## Testing

```sh
pipenv run test

curl http://localhost:5000/
curl http://localhost:5000/api/health
curl http://localhost:5000/api/ready
```

## Created

```sh
# install
pipenv install --dev flake8 flake8-bugbear flake8-2020 black
pipenv install --dev pytest 

pipenv install pyyaml python-json-logger flask python-dotenv ptvsd

pipenv install swagger-ui-bundle  
```

## Resources

https://www.imaginarycloud.com/blog/flask-python/

https://github.com/chrisguest75/banner_service/blob/master/Pipfile

https://stackoverflow.com/questions/67849806/flask-how-to-automate-openapi-v3-documentation

https://github.com/spec-first/connexion/issues/779