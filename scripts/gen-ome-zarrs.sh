#!/usr/bin/env bash

set -e

version=0.4
chunks=64
chunks_per_shard=0

input_dir="data/open-scivis-datasets"
output_dir="data/ome-zarr-open-scivis-datasets/v${version}/${chunks}x${chunks_per_shard}"
datasets_json="data/open-scivis-datasets/datasets.json"

mkdir -p $output_dir

chunks_per_shard_args=()
if [ "$chunks_per_shard" -gt 1 ]; then
  chunks_per_shard_args=("--chunks-per-shard" "$chunks_per_shard")
fi

# Iterate over all *.nhdr files in the data/open-scivis-datasets/**/*.nhdr directory
# and run the `ngff-zarr` cli on the files to output the OME-Zarr for mat in the directory
# ome-zarr-open-scivis-datasets/*.ome.zarr
for f in ${input_dir}/**/*.nhdr; do
  echo "Processing $f..."
  name=$(basename $f .nhdr)
  ngff-zarr \
    --method dask_image_gaussian \
    --input-backend itk \
    --chunks 64 \
    ${chunks_per_shard_args[@]} \
    --name $name \
    -i $f \
    -o ${output_dir}/${name}.ome.zarr
done
