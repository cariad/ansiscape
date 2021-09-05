#!/bin/env bash
set -euo pipefail

find . -name "*.sh" -not -path "*/.venv/*" -exec shellcheck -o all --severity style -x {} +

yamllint --strict .

if [ "${CI:=}" == "true" ]; then
  isort . --check-only --diff
else
  isort .
fi

if [ "${CI:=}" == "true" ]; then
  black . --check --diff
else
  black .
fi

flake8 .
mypy ansiscape
mypy tests
