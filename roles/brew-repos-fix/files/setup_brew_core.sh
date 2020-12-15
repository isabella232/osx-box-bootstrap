#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)
local_mirror=~/mirrors/github.com/bitrise-io/homebrew-core

rm -rf "$brew_repository/Library/Taps/homebrew"

rm -rf "${local_mirror}"

mkdir -p ~/mirrors/github.com/bitrise-io/

git clone --bare https://github.com/bitrise-io/homebrew-core "${local_mirror}"

git -C "${local_mirror}" fetch --unshallow

export HOMEBREW_CORE_GIT_REMOTE="${local_mirror}"

brew install a || true
