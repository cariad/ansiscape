#!/bin/env bash

set -euo pipefail

if [[ -n ${1:-} ]]; then
  version=${1}
elif [[ -n ${TAG_NAME:-} ]]; then
  version=${TAG_NAME}
else
  version="1.0.0"
fi

echo "${version}" > ansiscape/version/VERSION
rm -rf dist
python setup.py bdist_wheel
rm -rf build
