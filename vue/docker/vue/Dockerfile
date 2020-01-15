FROM node:13-alpine
MAINTAINER Yves Serrano <ys@taywa.ch>

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# essential layer
RUN apk add --update \
        curl \
        yarn \
        make
ADD yarn.lock package.json /opt/vue/
RUN mkdir -p /opt/vue /node_modules && ln -s /node_modules /opt/vue/node_modules

# vue/node layer
RUN apk add --update \
        build-base \
    && npm install -g @vue/cli && npm install -g http-server \
    && cd /opt/vue && yarn install \
    && apk del \
        build-base
RUN cd /opt/vue && yarn install

EXPOSE 8080
