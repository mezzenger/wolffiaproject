#!/usr/bin/env bash
set -euo pipefail
site_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
python3 "$site_dir/tests/check-site.py"
