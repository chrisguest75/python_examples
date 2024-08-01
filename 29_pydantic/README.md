# 29_pydantic

Demonstrate 29_pydantic

## Prepare

If using `vscode` remember to set your interpreter location to `.venv/bin/python`

## Start

```sh
export PIPENV_VENV_IN_PROJECT=1
# install
pipenv install --dev

# lint and test code
pipenv run format
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

- PyWhy use Pydantic? [here](https://docs.pydantic.dev/latest/why/)
- Pydantic object has no attribute '**fields_set**' error [here](https://stackoverflow.com/questions/73664830/pydantic-object-has-no-attribute-fields-set-error)
