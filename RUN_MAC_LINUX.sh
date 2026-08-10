#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
if command -v python3 >/dev/null 2>&1; then
  python3 RUN_SEXA_MASTER_AUDIT.py
else
  python RUN_SEXA_MASTER_AUDIT.py
fi
echo "Audit complete. See the reports folder."
