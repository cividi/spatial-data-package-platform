# syntax=docker/dockerfile:experimental
FROM alpine:3.11.3
MAINTAINER Yves Serrano <ys@taywa.ch>

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV YARN_CACHE_FOLDER /tmp/yarn_cache

# essential layer
RUN apk add --no-cache \
        curl \
        nodejs \
        yarn \
        make
RUN mkdir -p /opt/vue /node_modules /tmp/yarn_cache && ln -s /node_modules /opt/vue/node_modules
WORKDIR /opt/vue/

# vue/node layer 00
COPY ./package/00/package.json ./package/00/yarn.lock /opt/vue/
RUN --mount=type=cache,target=/tmp/yarn_cache \
    yarn global add --ignore-optional @vue/cli \
    && yarn global add --ignore-optional http-server \
    && yarn install --ignore-optional

# vue/node layer 01
# COPY ./package/01/package.json ./package/01/yarn.lock /opt/vue/
# RUN --mount=type=cache,target=/tmp/yarn_cache \
#     yarn install --ignore-optional

EXPOSE 8080
