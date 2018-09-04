
FROM python:3.7.0-alpine3.8
LABEL maintainer="Paolo <paolo@proofmedia.io>"

RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk add --no-cache libpng freetype libstdc++

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --no-cache --virtual .build-deps \
        musl-dev g++ \
        libpng-dev freetype-dev \
    && pip install --no-cache-dir --upgrade \
        --no-cache-dir --upgrade \
        -r /tmp/requirements.txt \
    && apk del .build-deps

ENV JUPYTER_CONFIG_FILE /root/.jupyter/jupyter_notebook_config.py

RUN mkdir -p /root/.jupyter \
    && echo "from notebook.auth import passwd" \
        > $JUPYTER_CONFIG_FILE \
    && echo "c.NotebookApp.password = passwd('proofmedia')" \
        >> $JUPYTER_CONFIG_FILE
