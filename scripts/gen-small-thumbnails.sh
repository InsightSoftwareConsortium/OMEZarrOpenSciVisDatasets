#!/usr/bin/env bash

set -e

mkdir -p thumbnails/small

for file in thumbnails/*.png; do
  cwebp -resize 480 0 $file -o thumbnails/small/$(basename $file .png).webp
done