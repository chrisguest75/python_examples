# syntax=docker/dockerfile:1.4
FROM python:3.11.3-slim-buster AS build-env

RUN pip install pipenv

ARG USERID=1000
ARG GROUPID=1000
RUN addgroup --system --gid $GROUPID appuser
RUN adduser --system --uid $USERID --gid $GROUPID appuser

WORKDIR /workbench
COPY ./Pipfile /workbench/Pipfile
COPY ./Pipfile.lock /workbench/Pipfile.lock 

#RUN set -ex && pipenv install --deploy --system
RUN pipenv install --deploy --system --dev

# RUN PIPENV_VENV_IN_PROJECT=1 pipenv run test

COPY ./tests /workbench/tests
COPY ./main.py /workbench

USER appuser
CMD ["python", "main.py"]

