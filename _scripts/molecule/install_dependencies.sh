#!/bin/bash

set -eo pipefail

script_full_path=$(dirname "$0")
os="$(uname -s)"

if [[ "$os" != "Darwin" ]]; then
    # build runs in ubuntu 16.04, python 3.5 is installed there, but it is not compatible with molecule
    add-apt-repository -y ppa:deadsnakes/ppa

    echo "Updating apt..."
    apt-get update &>/dev/null

    apt-get install -y python3.8 python3.8-dev python3.8-venv
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
    update-alternatives --set python3 /usr/bin/python3.8
    curl https://bootstrap.pypa.io/get-pip.py | python3.8

    echo "Install apt dependencies..."
    apt-get install -y build-essential libssl-dev libffi-dev &>"$BITRISE_DEPLOY_DIR"/apt_install.log

    pip_version="$(pip --version | awk '{print $1, $2}')"
    echo "Installed $pip_version"
fi


python3 -m venv ~/.venv/molecule
source ~/.venv/molecule/bin/activate

pip install -r "${script_full_path}/requirements.txt" --log "$BITRISE_DEPLOY_DIR"/pip_install.log

molecule_version="$(molecule --version | sed -n 1p)"
echo "Successfully installed $molecule_version"
