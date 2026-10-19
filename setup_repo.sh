#!/usr/bin/env bash
# Usage: ./setup_repo.sh <remote-url>
set -e
git init -b main
git add .
git commit -m "T03: initial repo structure and environment"
if [ -n "$1" ]; then
  git remote add origin "$1"
  git push -u origin main
fi
