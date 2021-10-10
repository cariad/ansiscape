#!/bin/env bash
set -euo pipefail

pytest -vv
dinject README.md docs/cli.md docs/read.md
