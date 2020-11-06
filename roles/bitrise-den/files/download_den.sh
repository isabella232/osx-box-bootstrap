#!/bin/bash
# fail if any commands fails
set -e
set -x
set -u

DOWNLOAD_URL=$(curl -s -n \
  --header "Authorization: token ${GITHUB_ACCESS_TOKEN}" \
  https://api.github.com/repos/bitrise-io/den/releases/${BITRISE_DEN_VERSION} \
  | jq '.assets[] | select(.name | contains("bitrise-den-darwin-amd64")) | .url' -r)

curl -s -n --show-error \
  --header "Authorization: token ${GITHUB_ACCESS_TOKEN}" \
  --header "Accept: application/octet-stream" \
  --request GET \
  --location \
  --output /var/tmp/bitrise-den-darwin-amd64.zip
