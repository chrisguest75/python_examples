# syntax=docker/dockerfile:1.4
FROM python:3.11.3-slim-bullseye AS build-env
#FROM pypy:3.10-7.3.17-bookworm AS build-env

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

#RUN set -ex && pipenv install --deploy --system
RUN pipenv install --deploy --system --dev

# RUN PIPENV_VENV_IN_PROJECT=1 pipenv run test
COPY --chmod=755 <<EOF /workbench/.env
export TEST_CONFIG="This is a test value from .env"
EOF

RUN chown -R appuser:appuser /workbench
COPY ./sources/LNL301_1mins.mp3 /workbench/sources/
COPY ./tests /workbench/tests
COPY ./logging_config.yaml /workbench
COPY ./main.py /workbench

# TODO: workout how to share in folders can be wrriten to by the user
#USER appuser
RUN mkdir -p /workbench/out 

COPY --chmod=755 <<EOF /workbench/start.sh
#!/usr/bin/env bash
. ./.env
env
pip list
python -m cProfile -o /workbench/out/main_cpu.pstats main.py --test \$@
EOF

CMD ["./start.sh"]

