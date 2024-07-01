# torch_package_client

Demonstrate torch_package_client

## Prepare

Configure CODEARTIFACT_URL.  

```sh
export AWS_PROFILE=my-profile
export AWS_REGION=us-east-1 
export PAGER=

aws codeartifact list-repositories   

export CODEARTIFACT_DOMAIN=chris-codeartifact-domain
export CODEARTIFACT_DOMAIN_OWNER=000000000000
export CODEARTIFACT_REPOSITORY=codeartifact-python-test

export CODEARTIFACT_AUTHTOKEN=$(aws --profile $AWS_PROFILE codeartifact get-authorization-token --domain $CODEARTIFACT_DOMAIN --domain-owner $CODEARTIFACT_DOMAIN_OWNER --query authorizationToken --output text)
export CODEARTIFACT_URL="https://aws:${CODEARTIFACT_AUTHTOKEN}@${CODEARTIFACT_DOMAIN}-${CODEARTIFACT_DOMAIN_OWNER}.d.codeartifact.${AWS_REGION}.amazonaws.com/pypi/${CODEARTIFACT_REPOSITORY}/simple/"
echo $CODEARTIFACT_URL
```

## Start

```sh
# install
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev --verbose

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

* Fix the pip error: Couldn't find a version that satisfies the requirement [here](https://bhch.github.io/posts/2017/04/fix-the-pip-error-couldnt-find-a-version-that-satisfies-the-requirement/)
