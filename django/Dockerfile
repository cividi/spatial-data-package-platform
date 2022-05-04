FROM alpine:3.13.7
MAINTAINER Yves Serrano <ys@taywa.ch>
# https://github.com/just-containers/s6-overlay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# essential layer
RUN apk add --no-cache \
        curl \
        libpq \
        python3 \
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
        freetype \
        lcms2 \
        libimagequant \
        libjpeg-turbo \
        libxcb \
        musl \
        openjpeg \
        py3-olefile \
        tiff \
        zlib \
        zlib-dev \
        sqlite-dev \
        yaml-dev \
        libressl-dev \
        yajl-dev \
    && curl -s https://bootstrap.pypa.io/get-pip.py | python3
ARG S6_OVERLAY_VERSION=v2.2.0.3
RUN curl -Ls https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz | tar xz -C /

# python requirements 00 layer
COPY docker/django/requirements/00/requirements.txt /tmp/requirements.txt
RUN apk add --no-cache \
        libjpeg-turbo-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        zlib-dev \
    && cd /opt && pip3 install --use-deprecated=legacy-resolver -r /tmp/requirements.txt \
    && apk del \
        libjpeg-turbo-dev \
        freetype-dev \
        lcms2-dev \
        openjpeg-dev \
        tiff-dev \
        zlib-dev \
    && pip3 cache purge

RUN apk add --update tzdata

COPY fixtures-tests     /opt/app/fixtures-tests/
COPY gsmap              /opt/app/gsmap/
COPY gsuser             /opt/app/gsuser/
COPY locale             /opt/app/locale/
COPY main               /opt/app/main/
COPY __init__.py        /opt/app/__init__.py
COPY conftest.py        /opt/app/conftest.py
COPY manage.py          /opt/app/manage.py
COPY pytest.ini         /opt/app/pytest.ini
COPY VERSION            /opt/app/VERSION

COPY docker/django/s6/etc/services.d /etc/services.d
COPY docker/django/s6/etc/cont-init.d /etc/cont-init.d
ENTRYPOINT ["/init"]

EXPOSE 8081
