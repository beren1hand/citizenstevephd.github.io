#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v bundle >/dev/null 2>&1; then
  echo "error: bundler not found. Install Ruby, then: gem install bundler" >&2
  exit 1
fi

bundle install
# Optional: ./serve.sh --livereload   (reload browser on file changes)
exec bundle exec jekyll serve "$@"
