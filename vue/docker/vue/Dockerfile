FROM node:13-alpine
MAINTAINER Yves Serrano <ys@taywa.ch>
ARG S6_OVERLAY_VERSION=v1.22.1.0
# https://github.com/just-containers/s6-overlay

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# essential layer
RUN apk add --update \
        curl \
        yarn \
        make
RUN mkdir -p /opt/vue /node_modules && ln -s /node_modules /opt/vue/node_modules
RUN curl -Ls -o /tmp/s6-overlay.tar.gz https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz \
    && tar xvfz /tmp/s6-overlay.tar.gz -C / \
    && rm -f /tmp/s6-overlay.tar.gz

# vue/node layer
# RUN apk add --update \
#         build-base
# RUN npm install -g @vue/cli && npm install -g http-server && mkdir -p /opt/vue/
# COPY yarn.lock package.json /opt/vue/
# RUN cd /opt/vue && yarn install



# ADD s6/etc/services.d /etc/services.d
# ADD s6/etc/cont-init.d /etc/cont-init.d
# ENTRYPOINT ["/init"]

EXPOSE 8080
