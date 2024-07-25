# syntax=docker/dockerfile:1.4
FROM python:3.11.9-slim-bullseye AS build-env

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

ARG USERID=1000
ARG GROUPID=1000
RUN addgroup --system --gid $GROUPID appuser
RUN adduser --system --uid $USERID --gid $GROUPID appuser

WORKDIR /workbench
COPY ./Pipfile /workbench/Pipfile
COPY ./Pipfile.lock /workbench/Pipfile.lock 

ENV TEST_CONFIG="This is a test value from .env"
COPY <<EOF /workbench/.env
export TEST_CONFIG="This is a test value from .env"
EOF

#RUN set -ex && pipenv install --deploy --system
RUN pipenv install --deploy --system --dev

# RUN PIPENV_VENV_IN_PROJECT=1 pipenv run test

COPY ./tests /workbench/tests
COPY ./main.py /workbench
COPY ./logging_config.yaml /workbench

USER appuser
#CMD ["python", "main.py"]
CMD ["fastapi", "run", "main.py"]

