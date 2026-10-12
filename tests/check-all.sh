#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
./tests/check-site.sh
python3 tools/build.py
python3 tests/check-production.py
