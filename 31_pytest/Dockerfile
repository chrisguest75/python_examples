# syntax=docker/dockerfile:1.4
ARG PYTHON_VERSION=3.11.8
FROM python:${PYTHON_VERSION}-slim as BUILDER
LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="31_pytest" dockerfile.stage="BUILDER"

###########################################
## Build and test
###########################################

ENV DEBIAN_FRONTEND=noninteractive
# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    --mount=type=tmpfs,target=/tmp \ 
    apt-get update \
    && apt-get install -fy -qq --no-install-recommends gettext 
#&& apt-get clean \
#&& rm -rf /var/lib/apt/lists/*

RUN pip install pipenv

WORKDIR /scratch
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock 

# # NOTE: Escape the \$ otherwise they are rendered at buildtime
# COPY --chmod=755 <<EOF /scratch/render-requirements.sh
# #!/usr/bin/env bash
# pipenv requirements | envsubst > ./requirements.txt
# EOF

ENV PIPENV_VENV_IN_PROJECT=1
RUN --mount=type=cache,target=/root/.cache/pip \
    pipenv install --dev

COPY ./.flake8 ./setup.cfg ./logging_config.yaml /scratch/
COPY ./tests /scratch/tests
COPY ./bubblesort.py ./directory_trie.py ./main.py /scratch/

RUN pipenv run lint
RUN pipenv run test
RUN pipenv run test:coverage:build
RUN pipenv check

###########################################
## Final image
###########################################

FROM python:${PYTHON_VERSION}-slim as PRODUCTION
LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="31_pytest" dockerfile.stage="PRODUCTION"

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser --disabled-password --gecos "" --home "/nonexistent" --shell "/sbin/nologin" --no-create-home --uid "${UID}" appuser

WORKDIR /scratch
USER appuser

COPY --chmod=755 <<EOF /scratch/start-app.sh
#!/usr/bin/env bash
export PATH="/scratch/.venv/bin:$PATH"
export TEST_CONFIG="This is a test value from .env"
python main.py --test
EOF

# NOTE: This still has dev packages...
COPY --from=BUILDER /scratch/.venv /scratch/.venv
COPY --from=BUILDER /scratch/logging_config.yaml /scratch/logging_config.yaml
COPY --from=BUILDER /scratch/bubblesort.py /scratch/directory_trie.py /scratch/main.py /scratch/
CMD ["/scratch/start-app.sh"]
