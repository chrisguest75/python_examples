FROM ubuntu:22.04 AS prebuild

ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ARG DEBIAN_FRONTEND=noninteractive

RUN rm -f /etc/apt/apt.conf.d/docker-clean; \
    echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' \
    > /etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y bash curl git nano locales apt-transport-https make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev xz-utils libxml2-dev libxmlsec1-dev 

RUN locale-gen en_US.UTF-8  

# pyenv
# ARG USERID=1000
# ARG GROUPID=1000
# RUN addgroup --system --gid $GROUPID appuser
# RUN adduser --system --uid $USERID --gid $GROUPID appuser

# ENV HOME /home/appuser
ENV HOME /home/root
WORKDIR $HOME
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv

ARG PYTHON_VERSION=3.11.9
WORKDIR /workbench
RUN echo "$PYTHON_VERSION" > /workbench/.python-version

#USER appuser

ENV PYENV_ROOT="$HOME/.pyenv" 
ENV PATH="$PYENV_ROOT/bin:$PATH"
RUN pyenv install $(cat /workbench/.python-version)
RUN pyenv global $(cat /workbench/.python-version)

RUN pyenv exec pip3 install pipenv wheel setuptools

FROM prebuild AS builder
WORKDIR /scratch
RUN git clone --recursive https://github.com/SYSTRAN/faster-whisper

COPY --chmod=755 <<EOF /scratch/build.sh
#!/usr/bin/env bash
cd faster-whisper
pyenv exec python3 setup.py sdist bdist_wheel

cp dist /out/ -r
cp faster_whisper.egg-info /out/ -r
EOF

CMD ["/scratch/build.sh"]
