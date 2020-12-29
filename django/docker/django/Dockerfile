FROM alpine:3.12.3
MAINTAINER Yves Serrano <ys@taywa.ch>
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
        bash \
        build-base \
        python3-dev \
        gdal \
        geos \
        proj \
        yajl \
        proj-datumgrid \
        zlib-dev \
        sqlite-dev \
        yaml-dev \
        libressl-dev \
        yajl-dev \
    && curl -s https://bootstrap.pypa.io/get-pip.py | python3
ARG S6_OVERLAY_VERSION=v2.1.0.2
RUN curl -Ls https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz | tar xz -C /

# python requirements 00 layer
COPY ./requirements/00.txt /tmp/requirements.txt
RUN cd /opt && pip3 install -r /tmp/requirements.txt

# python requirements 03 layer, django DRF, django-apscheduler
COPY ./requirements/03.txt /tmp/requirements.txt
RUN cd /opt && pip3 install -r /tmp/requirements.txt

COPY s6/etc/services.d /etc/services.d
COPY s6/etc/cont-init.d /etc/cont-init.d
ENTRYPOINT ["/init"]

EXPOSE 8081
