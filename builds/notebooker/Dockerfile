FROM python:3.7.1
LABEL maintainer="Paolo <paolo@proofmedia.io>"

WORKDIR /tmp
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENV JUPYTER_CONFIG_FILE /root/.jupyter/jupyter_notebook_config.py
ENV NOTEBOOK_PASSWORD somenicelongerpassw
RUN mkdir -p /root/.jupyter

RUN mkdir /docker-entrypoint.d/
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/*
CMD ["docker-entrypoint"]

VOLUME /app
WORKDIR /app
