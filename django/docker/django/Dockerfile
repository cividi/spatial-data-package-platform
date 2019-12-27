FROM alpine:3.10
MAINTAINER Yves Serrano <ys@taywa.ch>
ARG S6_OVERLAY_VERSION=v1.22.1.0
# https://github.com/just-containers/s6-overlay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# essential layer
RUN apk add --update \
        curl \
        libpq \
        python3 \
        libressl \
        make
RUN curl -Ls -o /tmp/s6-overlay.tar.gz https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz \
    && tar xvfz /tmp/s6-overlay.tar.gz -C / \
    && rm -f /tmp/s6-overlay.tar.gz \
    && pip3 install --upgrade pip

# python requirements layer
ADD ./requirements.txt /tmp/
RUN apk add \
        git \
        autoconf \
        automake \
        build-base \
        ncurses-dev \
        python3-dev \
        zlib-dev \
        sqlite-dev \
        yaml-dev \
        g++ \
        gcc \
        postgresql-dev \
        libressl-dev \
    && pip3 install -r /tmp/requirements.txt \
    && apk del \
        autoconf \
        automake \
        build-base \
        ncurses-dev \
        python3-dev \
        zlib-dev \
        sqlite-dev \
        yaml-dev \
        g++ \
        gcc \
        postgresql-dev \
        libressl-dev \
    && apk add libstdc++ \
    && rm -rf /var/cache/apk/* /tmp/*

# ADD s6/etc/services.d /etc/services.d
# ADD s6/etc/cont-init.d /etc/cont-init.d
# ENTRYPOINT ["/init"]

EXPOSE 8081
