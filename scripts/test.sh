#!/usr/bin/env bash
set -euo pipefail

echo "[check] lint"
ruff check .

echo "[check] test"
pytest

echo "[ok] all checks passed"
