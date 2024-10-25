# syntax=docker/dockerfile:1.4
ARG BASE_IMAGE=python:3.11.3-slim-buster
FROM ${BASE_IMAGE} AS build-env

RUN apt-get update \
    && apt-get install -fy -qq --no-install-recommends libomp5 cmake curl ca-certificates \
    && apt-get clean 

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
COPY ./packages /workbench/packages
COPY ./Pipfile /workbench/Pipfile
COPY ./Pipfile.lock /workbench/Pipfile.lock 

#RUN set -ex && pipenv install --deploy --system
#RUN pipenv lock
RUN pipenv install --deploy --system --dev

RUN mkdir -p ./model && curl -o ./model/transformer-ende-wmt-pyOnmt.tar.gz https://s3.amazonaws.com/opennmt-models/transformer-ende-wmt-pyOnmt.tar.gz

# COPY --chmod=755 <<EOF /workbench/getmodel.sh
# #!/usr/bin/env bash
# cd ./model
# tar xf ./transformer-ende-wmt-pyOnmt.tar.gz
# cd ..
# pipenv run ct2-opennmt-py-converter --model_path ./model/averaged-10-epoch.pt --output_dir ./model/ende_ctranslate2
# EOF
# RUN /workbench/getmodel.sh
COPY model ./model

# RUN PIPENV_VENV_IN_PROJECT=1 pipenv run test
COPY --chmod=755 <<EOF /workbench/.env
export TEST_CONFIG="This is a test value from .env"
EOF

COPY ./tests /workbench/tests
COPY ./logging_config.yaml /workbench
COPY ./main.py /workbench
RUN cp /workbench/packages/build/libctranslate2.so /usr/local/lib/libctranslate2.so.4

#USER appuser

COPY --chmod=755 <<EOF /workbench/start.sh
#!/usr/bin/env bash
. ./.env
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
env
pip list
python main.py --test
EOF

CMD ["./start.sh"]

