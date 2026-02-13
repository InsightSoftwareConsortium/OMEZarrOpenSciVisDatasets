#!/usr/bin/env bash

set -e

# Default values
version_default="0.4"
chunks_default=64
chunks_per_shard_default=0
ozx_default=false

# Initialize variables with default values
version="$version_default"
chunks="$chunks_default"
chunks_per_shard="$chunks_per_shard_default"
ozx="$ozx_default"

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -v|--version) version="$2"; shift ;;
        -c|--chunks) chunks="$2"; shift ;;
        -s|--chunks-per-shard) chunks_per_shard="$2"; shift ;;
        --ozx) ozx=true ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

input_dir="data/open-scivis-datasets"
output_dir="data/ome-zarr-open-scivis-datasets/v${version}/${chunks}x${chunks_per_shard}"
datasets_json="data/open-scivis-datasets/datasets.json"

# Add -ozx to output_dir if ozx mode is enabled
if [ "$ozx" = true ]; then
  output_dir="${output_dir}-ozx"
fi

mkdir -p $output_dir

chunks_per_shard_args=()
if [ "$chunks_per_shard" -gt 0 -a "$version" == "0.4" ]; then
  chunks_per_shard_args=("--chunks-per-shard" "$chunks_per_shard")
fi

# Iterate over all *.nhdr files in the data/open-scivis-datasets/**/*.nhdr directory
# and run the `ngff-zarr` cli on the files to output the OME-Zarr for mat in the directory
# ome-zarr-open-scivis-datasets/*.ome.zarr or *.ozx
for f in ${input_dir}/**/*.nhdr; do
  echo "Processing $f..."
  name=$(basename $f .nhdr)

  # Set output extension based on ozx flag
  if [ "$ozx" = true ]; then
    output_ext=".ozx"
  else
    output_ext=".ome.zarr"
  fi

  ngff-zarr \
    --method dask_image_gaussian \
    --omero-dense \
    --input-backend itk \
    --chunks "$chunks" \
    --ome-zarr-version "${version}" \
    ${chunks_per_shard_args[@]} \
    --name "$name" \
    -i "$f" \
    -o "${output_dir}/${name}${output_ext}"
done
