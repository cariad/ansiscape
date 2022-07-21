#!/bin/env bash

set -euo pipefail

assert() {
  if [[ "${1}" == "${2}" ]]; then
    return
  fi

  echo "Expected \"${2}\" but got \"${1}\" 🔥"
  exit 1
}

# shellcheck disable=SC2312
assert "$(ansiscape --version)"        "${CIRCLE_TAG:-"-1.-1.-1"}"

# shellcheck disable=SC2312
assert "$(ansiscape --check)"          "no"

# shellcheck disable=SC2312
assert "$(naughtty ansiscape --check)" $'yes\r'
