
FROM python:3.7.0-alpine3.8
LABEL maintainer="Paolo <paolo@proofmedia.io>"

##############
RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk add --no-cache libpng freetype libstdc++ libxslt libxml2
    # libxml2

COPY ./requirements.txt /tmp/requirements.txt
RUN apk add --no-cache --virtual .build-deps \
        musl-dev gcc g++ libxslt-dev libxml2-dev \
        libpng-dev freetype-dev \
    && pip install --no-cache-dir --upgrade \
        -r /tmp/requirements.txt \
    && apk del .build-deps
    # libxml2-dev \
# bug above

##############
RUN apk add --no-cache git

RUN mkdir /docker-entrypoint.d/
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/*

ENV JUPYTER_CONFIG_FILE /root/.jupyter/jupyter_notebook_config.py
ENV NOTEBOOK_PASSWORD somenicelongerpassw
RUN mkdir -p /root/.jupyter

WORKDIR /tmp
COPY ./extra-requirements.txt dev-requirements.txt
RUN pip3 install --upgrade -r dev-requirements.txt

VOLUME /app
WORKDIR /app
CMD ["docker-entrypoint"]
