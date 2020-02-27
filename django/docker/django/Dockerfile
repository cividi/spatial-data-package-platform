FROM alpine:3.11
MAINTAINER Yves Serrano <ys@taywa.ch>
ARG S6_OVERLAY_VERSION=v1.22.1.0
# https://github.com/just-containers/s6-overlay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# essential layer
RUN apk add --no-cache \
        curl \
        libpq \
        python3 \
        py3-pillow \
        py3-gunicorn \
        py3-psycopg2 \
        jq \
        libressl \
        make \
        git \
        autoconf \
        automake \
        libstdc++ \
    && pip3 install --upgrade pip \
    && mkdir -p /tmp/requirements
RUN curl -Ls https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz | tar xz -C /

# dev libs
RUN apk add --no-cache \
        zlib-dev \
        sqlite-dev \
        yaml-dev \
        libressl-dev

# python requirements 00 layer
COPY ./requirements/00.txt /tmp/requirements.txt
RUN apk add --no-cache build-base python3-dev \
    && pip3 install -r /tmp/requirements.txt \
    && apk del build-base python3-dev

# geodjango layer
RUN apk --no-cache add gdal geos proj proj-datumgrid

COPY s6/etc/services.d /etc/services.d
COPY s6/etc/cont-init.d /etc/cont-init.d
ENTRYPOINT ["/init"]

EXPOSE 8081
