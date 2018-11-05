
FROM python:3.7.1-alpine3.8
LABEL maintainer="Paolo <paolo@proofmedia.io>"

RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk add --no-cache \
        git \
        libpng freetype libstdc++ libxslt libxml2

WORKDIR /tmp
COPY ./requirements.txt requirements.txt
RUN apk add --no-cache --virtual .build-deps \
        musl-dev gcc g++ libxslt-dev libxml2-dev \
        libpng-dev freetype-dev \
    && pip install --no-cache-dir --upgrade \
        -r requirements.txt \
    && apk del .build-deps

COPY ./extra-requirements.txt dev-requirements.txt
RUN pip install --upgrade --no-cache-dir \
    -r dev-requirements.txt

ENV JUPYTER_CONFIG_FILE /root/.jupyter/jupyter_notebook_config.py
ENV NOTEBOOK_PASSWORD somenicelongerpassw
RUN mkdir -p /root/.jupyter

RUN mkdir /docker-entrypoint.d/
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/*
CMD ["docker-entrypoint"]
VOLUME /app
WORKDIR /app
