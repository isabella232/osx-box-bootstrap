#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

rm -rf "$brew_repository/Library/Taps/homebrew"

mkdir -p ~/mirrors/github.com/bitrise-io/

git clone --bare https://github.com/bitrise-io/homebrew-core ~/mirrors/github.com/bitrise-io/homebrew-core

export HOMEBREW_CORE_GIT_REMOTE="~/mirrors/github.com/bitrise-io/homebrew-core"

brew install a || true
