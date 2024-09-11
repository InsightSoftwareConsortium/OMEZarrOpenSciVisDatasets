#!/usr/bin/env bash

set -e

version=0.4

input_dir="data/open-scivis-datasets"
output_dir="data/ome-zarr-open-scivis-datasets/v${version}"
datasets_json="data/open-scivis-datasets/datasets.json"

mkdir -p $output_dir

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
    --name $name \
    -i $f \
    -o ${output_dir}/${name}.ome.zarr
done
