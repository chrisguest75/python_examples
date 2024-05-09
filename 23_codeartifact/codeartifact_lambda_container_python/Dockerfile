# syntax=docker/dockerfile:1.4
FROM python:3.11.3-slim-buster AS BUILDER
LABEL dockerfile.baseimage="python:3.11.3-slim-buster" dockerfile.description="24_lambda_container_python" dockerfile.stage="BUILDER"

RUN apt-get update \
    && apt-get install -fy -qq --no-install-recommends gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG CODEARTIFACT_URL
ENV CODEARTIFACT_URL=${CODEARTIFACT_URL}

RUN pip install pipenv

WORKDIR /scratch
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock 

# NOTE: Escape the \$ otherwise they are rendered at buildtime
COPY --chmod=755 <<EOF /usr/bin/render-requirements.sh
#!/usr/bin/env bash
pipenv requirements | envsubst > ./requirements.txt
EOF

#RUN set -ex && pipenv install --deploy --system
RUN /usr/bin/render-requirements.sh


COPY ./main.py  /scratch
COPY ./logging_config.yaml /scratch

########################

FROM public.ecr.aws/lambda/python:3.11 AS PRODUCTION
LABEL dockerfile.baseimage="public.ecr.aws/lambda/python:3.11" dockerfile.description="24_lambda_container_python" dockerfile.stage="PRODUCTION"

ENV NODE_ENV production

WORKDIR ${LAMBDA_TASK_ROOT}

COPY --from=BUILDER /scratch/ .
RUN pip install -r requirements.txt

CMD ["main.handler"]