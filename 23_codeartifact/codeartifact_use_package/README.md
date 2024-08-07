# codeartifact_use_package

Demonstrate codeartifact_use_package

## Start

Login

```sh
export AWS_PROFILE=my-profile
export AWS_REGION=us-east-1 
export PAGER=

aws codeartifact list-repositories
```

Configure profile.  

```sh
export CODEARTIFACT_DOMAIN=chris-codeartifact-domain
export CODEARTIFACT_DOMAIN_OWNER=000000000000
export CODEARTIFACT_REPOSITORY=codeartifact-python-test

export CODEARTIFACT_AUTHTOKEN=$(aws --profile $AWS_PROFILE codeartifact get-authorization-token --domain $CODEARTIFACT_DOMAIN --domain-owner $CODEARTIFACT_DOMAIN_OWNER --query authorizationToken --output text)
export CODEARTIFACT_URL="https://aws:${CODEARTIFACT_AUTHTOKEN}@${CODEARTIFACT_DOMAIN}-${CODEARTIFACT_DOMAIN_OWNER}.d.codeartifact.${AWS_REGION}.amazonaws.com/pypi/${CODEARTIFACT_REPOSITORY}/simple/"
echo $CODEARTIFACT_URL
```

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
