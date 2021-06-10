FROM python:3.9.5-slim-buster

ENV TZ JST-9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=on
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update -y \
    && apt-get install -y git curl make xz-utils file sudo \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

RUN mkdir /data
