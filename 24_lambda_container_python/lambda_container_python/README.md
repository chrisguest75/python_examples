# LAMBDA CONTAINER

Demonstrate how to build a Lambda Container

TODO:

* Use dockerfile excludes on copy files

## Start

```sh
# build and run the lambda locally
just docker_run

# invoke as a test
curl -XPOST "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{ "queryStringParameters": { "url": "https://www.google.com/" } }'
```

## Local

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

## Build Image

```sh
export AWS_ACCOUNTID=$(aws sts get-caller-identity --query "Account" --output text)
echo ${AWS_ACCOUNTID}
AWS_REGISTRY=${AWS_ACCOUNTID}.dkr.ecr.${AWS_REGION}.amazonaws.com

# log into registry
export AWS_REGISTRY=$(terraform output --json repository_url | jq -r '. | split("/") | .[0]')
echo $AWS_REGISTRY
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_REGISTRY}

docker buildx bake -f docker-bake.hcl --metadata-file ./bake-metadata.json  
docker buildx bake -f docker-bake.hcl --metadata-file ./bake-metadata.json --no-cache 

REGISTRY=${AWS_REGISTRY}/ docker buildx bake -f docker-bake.hcl --metadata-file ./bake-metadata.json --push
```

## Troubleshooting

```sh
# pull the base image
docker pull public.ecr.aws/lambda/python:3.11

# have a look at what is inside
dive public.ecr.aws/lambda/python:3.11

# copy lambda-entrypoint.sh
docker create --rm -it --name python311 public.ecr.aws/lambda/python:3.11
docker cp python311:/lambda-entrypoint.sh ./

# jump into the container 
docker exec -it 24_lambda_container_python /bin/bash

# inspect it
dive 24_lambda_container_python:latest
```

## Debugging and Troubleshooting

```sh
# enter python
pipenv run python

> import main

> main.test.__doc__
```

## Resources

- Base images for Lambda [here](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html)  
- Using an AWS base image for Python [here](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)  
- AWS Lambda NodeJS Runtime Interface Client [here](https://www.npmjs.com/package/aws-lambda-ric)  
- Lambda Internals: Exploring AWS Lambda [here](https://hackernoon.com/lambda-internals-exploring-aws-lambda-462f05f74076)  
- AWS Lambda Performance Tuning & Best Practices (2022) [here](https://www.simform.com/blog/aws-lambda-performance/)  
- Running Containers on AWS Lambda [here](https://earthly.dev/blog/aws-lambda-docker/)  
