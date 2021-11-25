# syntax=docker/dockerfile:experimental
FROM alpine:3.13.6
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
RUN mkdir -p /opt/vue /opt/node_modules /tmp/yarn_cache && echo '--modules-folder /opt/node_modules' >> /opt/vue/.yarnrc
COPY ./s6_download.sh /tmp/s6_download.sh
RUN chmod +x /tmp/s6_download.sh
ARG S6_OVERLAY_VERSION=v2.2.0.3
RUN sh /tmp/s6_download.sh

WORKDIR /opt/vue/

# puppeteer
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
RUN apk add --no-cache \
      rsync \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ttf-freefont

ENV PATH "/opt/node_modules/.bin/:$PATH"

# vue/node layer 00 / flatten all layers before, added vue-cookies
COPY ./package/00/package.json ./package/00/yarn.lock /opt/vue/
RUN --mount=type=cache,target=/tmp/yarn_cache \
    yarn global add --ignore-optional @vue/cli \
    && yarn global add --ignore-optional http-server \
    && yarn install

# vue/node layer 01 / dependabot updates
COPY ./package/01/package.json ./package/01/yarn.lock /opt/vue/
RUN --mount=type=cache,target=/tmp/yarn_cache \
    yarn install

COPY s6/etc/services.d /etc/services.d
COPY s6/etc/cont-init.d /etc/cont-init.d
ENTRYPOINT ["/init"]

EXPOSE 8080
