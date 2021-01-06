#!/bin/bash
set -eo pipefail

source ~/.venv/molecule/bin/activate

function setup_env {
    cp "molecule/$1/molecule.docker.yml" "molecule/$1/molecule.yml"
}

function run_test {
    molecule destroy -s "$1"
    molecule create -s "$1"
    molecule converge -s "$1"
    molecule verify -s "$1"
    molecule destroy -s "$1"
}

setup_env "${ROLE}"

run_test "${ROLE}" | tee "$BITRISE_DEPLOY_DIR/molecule.log"
