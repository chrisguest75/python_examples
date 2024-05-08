# syntax=docker/dockerfile:1.4
FROM python:3.11.3-slim-buster AS BUILDER
LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="24_lambda_container_python" dockerfile.stage="BUILDER"

RUN pip install pipenv

WORKDIR /scratch
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock 

#RUN set -ex && pipenv install --deploy --system
RUN pipenv requirements > /scratch/requirements.txt

COPY ./main.py  /scratch
COPY ./logging_config.yaml /scratch

FROM public.ecr.aws/lambda/python:3.11 AS PRODUCTION
LABEL dockerfile.baseimage="public.ecr.aws/lambda/python:3.11" dockerfile.description="24_lambda_container_python" dockerfile.stage="PRODUCTION"

ENV NODE_ENV production

WORKDIR ${LAMBDA_TASK_ROOT}

COPY --from=BUILDER /scratch/ .
RUN pip install -r requirements.txt

CMD ["main.handler"]