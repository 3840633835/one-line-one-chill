#!/bin/sh
# Determinism check: run main.py twice into two directories; outputs must
# be byte-identical, and must match the committed entry.txt exactly.
set -eu
cd "$(dirname "$0")"
rm -rf /tmp/one-line-one-chill-a /tmp/one-line-one-chill-b
OUTPUT_DIR=/tmp/one-line-one-chill-a python3 main.py
OUTPUT_DIR=/tmp/one-line-one-chill-b python3 main.py
cmp /tmp/one-line-one-chill-a/entry.txt /tmp/one-line-one-chill-b/entry.txt
cmp /tmp/one-line-one-chill-a/entry.txt entry.txt
echo "determinism OK: $(wc -c < entry.txt) bytes"
