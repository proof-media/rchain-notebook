
FROM python:3.7.0-alpine3.8
LABEL maintainer="Paolo <paolo@proofmedia.io>"

RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk add --no-cache \
        git \
        libpng freetype libstdc++ libxslt libxml2

WORKDIR /tmp
COPY ./requirements.txt requirements.txt
# Add build deps for numpy/pandas/matplotlib and remove them
RUN apk add --no-cache --virtual .build-deps \
        musl-dev gcc g++ libxslt-dev libxml2-dev \
        libpng-dev freetype-dev \
    && pip install --no-cache-dir --upgrade \
        -r requirements.txt \
    && apk del .build-deps
COPY ./extra-requirements.txt dev-requirements.txt
RUN pip install --upgrade --no-cache-dir \
    -r dev-requirements.txt

#########################
# HACK to skip issue:
# https://github.com/protocolbuffers/protobuf/issues/5272
ENV PYPPATHS /usr/local/lib/python3.7/site-packages
ENV PATCH_REPO pdonorio/protobuf/rchain-workaround
RUN cd $PYPPATHS/google/protobuf/internal/ \
    && rm python_message.py* \
    && wget -q https://raw.githubusercontent.com/$PATCH_REPO/python/google/protobuf/internal/python_message.py \
    && echo "protobuf patched"
#########################

ENV JUPYTER_CONFIG_FILE /root/.jupyter/jupyter_notebook_config.py
ENV NOTEBOOK_PASSWORD somenicelongerpassw
RUN mkdir -p /root/.jupyter

RUN mkdir /docker-entrypoint.d/
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/*
CMD ["docker-entrypoint"]
VOLUME /app
WORKDIR /app
