# syntax=docker/dockerfile:1.4
ARG PYTHON_VERSION=3.11.8
FROM python:${PYTHON_VERSION}-slim as BUILDER
LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="31_pytest" dockerfile.stage="BUILDER"

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -fy -qq --no-install-recommends gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /scratch
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock 

# # NOTE: Escape the \$ otherwise they are rendered at buildtime
# COPY --chmod=755 <<EOF /usr/bin/render-requirements.sh
# #!/usr/bin/env bash
# pipenv requirements | envsubst > ./requirements.txt
# EOF

# #RUN set -ex && pipenv install --deploy --system
# RUN /usr/bin/render-requirements.sh
RUN pipenv install --deploy --system --dev

COPY ./.flake8 ./setup.cfg ./logging_config.yaml ./main.py /scratch/
COPY ./bubblesort.py ./directory_trie.py /scratch/
COPY ./tests /scratch/tests

RUN pipenv run lint
RUN pipenv run test




########################

# FROM python:${PYTHON_VERSION}-slim as PRODUCTION
# LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="31_pytest" dockerfile.stage="PRODUCTION"

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser




# WORKDIR /scratch

# # Create a non-privileged user that the app will run under.
# # See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# # Download dependencies as a separate step to take advantage of Docker's caching.
# # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# # Leverage a bind mount to requirements.txt to avoid having to copy them into
# # into this layer.
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt

# # Switch to the non-privileged user to run the application.
# USER appuser

# # Copy the source code into the container.
# COPY . .

# # Expose the port that the application listens on.
# EXPOSE 8000

# # Run the application.
# CMD python main.py




