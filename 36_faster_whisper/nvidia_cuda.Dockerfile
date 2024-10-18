# syntax=docker/dockerfile:1.4
#FROM docker.io/nvidia/cuda:12.5.0-runtime-ubuntu22.04 AS build-env
#FROM docker.io/nvidia/cuda:12.6.1-cudnn-devel-ubuntu22.04 AS build-env
#FROM docker.io/nvidia/cuda:12.6.1-cudnn-runtime-ubuntu22.04 AS build-env
FROM docker.io/nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04 AS build-env


RUN apt-get update && apt-get install curl python3 python3-pip -y 

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
python3 -m cProfile -o /workbench/out/main_gpu.pstats main.py --test --gpu \$@
EOF

CMD ["./start.sh"]

