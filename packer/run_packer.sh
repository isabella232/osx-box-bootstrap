#!/bin/bash

if test z$1 = z ; then
  echo "Please pass a packer json file to build"
  exit 2
fi

export PACKER_LOG=0 # 1 to debug
export ANKA_DEFAULT_PASSWD=vagrant
export ANKA_DEFAULT_USER=vagrant

sudo -E packer build -color=true -timestamp-ui $1
# sudo -E packer build -debug -color=true -timestamp-ui $1
