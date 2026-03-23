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
assert "$(ansiscape --version)"        "${TAG_NAME:-"1.0.0"}"

# shellcheck disable=SC2312
assert "$(ansiscape --check)"          "no"

# shellcheck disable=SC2312
assert "$(naughtty ansiscape --check)" $'yes\r'
