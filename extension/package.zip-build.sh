#!/usr/bin/env bash
# Bundle the extension into a .zip suitable for Chrome Web Store / Edge Add-ons
# / Firefox AMO upload. Run from anywhere — the script cds into its own dir.
set -euo pipefail
cd "$(dirname "$0")"

VERSION=$(python3 -c "import json; print(json.load(open('manifest.json'))['version'])")
OUT="toolhub-extension-v${VERSION}.zip"

rm -f "$OUT"
zip -r "$OUT" \
  manifest.json \
  background.js \
  auto-detect.js \
  tool-map.js \
  icons \
  _locales \
  -x "*.DS_Store"

echo "Built: $OUT"
ls -la "$OUT"
