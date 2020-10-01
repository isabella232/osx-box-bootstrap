#!/bin/bash

set -e

source ~/.bash_profile

brew_repository=$(brew --repository)

mkdir -p ~/mirrors/github.com/bitrise-io/

git clone --bare https://github.com/bitrise-io/homebrew-cask ~/mirrors/github.com/bitrise-io/homebrew-cask

git clone ~/mirrors/github.com/bitrise-io/homebrew-cask "${brew_repository}/Library/Taps/homebrew/homebrew-cask"
