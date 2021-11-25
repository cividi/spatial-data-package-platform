#!/bin/bash
if [ $(uname -mm) = "x86_64" ]
then
    curl -Ls https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz | tar xz -C /
fi
if [ $(uname -mm) = "aarch64" ]
then
    curl -Ls https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-aarch64.tar.gz | tar xz -C /
fi