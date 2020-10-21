#!/bin/bash

usage() {
  echo $(basename "${0}") "packer_json xcode_version"
  exit 1
}

if test z$1 = z ; then
  usage
fi

if test z$2 = z ; then
  usage
fi

export XCODE_SEED=baseOS_10-15-7-1602690351

if test $2 = 11.6 ; then
  export SIMULATOR_SEED=baseXcode_11.6-1602757543
elif test $2 = 11.7 ; then
  export SIMULATOR_SEED=baseXcode_11.7-1602758063
fi

export PACKER_LOG=0 # 1 to debug
export ANKA_DEFAULT_PASSWD=vagrant
export ANKA_DEFAULT_USER=vagrant
export XCODE_VERSION=$2

sudo -E packer build -color=true -timestamp-ui $1
# sudo -E packer build -debug -color=true -timestamp-ui $1
