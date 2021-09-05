#!/bin/env bash

set -euo pipefail

if [[ -n ${1:-} ]]; then
  version=${1}
elif [[ -n ${CIRCLE_TAG:-} ]]; then
  version=${CIRCLE_TAG}
else
  version="-1.-1.-1"
fi

echo "${version}" > ansiscape/version/VERSION
rm -rf dist
python setup.py bdist_wheel
rm -rf build
