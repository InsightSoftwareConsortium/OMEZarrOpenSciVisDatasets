#!/usr/bin/env python3

import os
import re
import sys
import json

import ngff_zarr as nz
import zarr.storage

def get_datasets_json():
    input_datasets_json="data/open-scivis-datasets/datasets.json"
    with open(input_datasets_json, "r") as f:
        datasets = json.load(f)
    return datasets

DATASETS = get_datasets_json()
def get_datasets():
    # Remove currently unsupported
    DATASETS.pop("dns", None)
    DATASETS.pop("isotropic_pressure", None)
    DATASETS.pop("rotstrat_temperature", None)
    DATASETS.pop("3d_neurons_15_sept_2016", None)
    return DATASETS

def get_dataset_names():
    datasets = get_datasets()
    return datasets.keys()

def get_dataset(dataset_name):
    datasets = get_datasets()
    return datasets[dataset_name]



with open('./README.md', 'w') as fp:
    fp.write("# OME-Zarr Open SciVis Datasets\n")

    ome_zarr_intro = """
![engine](./thumbnails/small/engine.webp)

> The OME-Zarr Open SciVis Datasets project provides the Open SciVis Dataset in a chunked, multi-scale format, encodes metadata in JSON according to the OME-Zarr specification, and hosts the datasets on AWS S3 through the AWS Open Data Program, aiming to serve as a web-based resource for the scientific visualization community to enhance reproducibility and facilitate testing and development of OME-Zarr tools.

## Table of Contents

- [Introduction](#introduction)
  - [OME-Zarr](#ome-zarr)
  - [Open SciVis Datasets](#open-scivis-datasets)
  - [Project Overview](#project-overview)
- [Datasets](#datasets)
  - [Sorted by number of voxels](#sorted-by-number-of-voxels)
  - [CT Scans](#ct-scans)
  - [MRI Scans](#mri-scans)
  - [Microscopy Datasets](#microscopy-datasets)
  - [Simulation Datasets](#simulation-datasets)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

### OME-Zarr

[OME-Zarr](https://ngff.openmicroscopy.org/) is a cloud-optimized bioimaging
file format that has emerged as a promising solution to address the challenges
of scalability and heterogeneity in scientific data exchange. Developed by the
Open Microscopy Environment (OME) in collaboration with an international
community of researchers and institutions, OME-Zarr builds upon the Zarr format
to provide a flexible and scalable method for storing multidimensional imaging
data and associated metadata.

The format is designed to support both pixel measurements and relevant imaging
metadata, including experimental, acquisition, and analytic information.
OME-Zarr offers significant advantages over traditional formats like TIFF and
HDF5, particularly in its ability to efficiently handle large, multi-Gigabyte to
Petabyte datasets in cloud-based storage environments. By storing data in
individually referenceable "chunk" files, OME-Zarr enables fast, random access
to specific portions of large datasets without requiring access to the entire
file.

Since its initial publication in 2021, OME-Zarr has seen rapid adoption and
expansion of supporting tools. The format now accommodates a wide range of
bioimaging modalities and derived data types, such as regions of interest (ROIs)
and segmentation labels. This growth has been driven by an open, collaborative
development process that brings together diverse use cases and requirements from
across the bioimaging community. As a result, OME-Zarr is emerging as a unifying
format that promotes FAIR (Findable, Accessible, Interoperable, and Reusable)
data principles in the bioimaging domain, facilitating more efficient data
management, analysis, and sharing across personal, institutional, and global
scales.

For more information about OME-Zarr, including the latest specifications,
reference implementations, and community resources, please visit the [OME-Zarr
website](https://ngff.openmicroscopy.org/), including the [reference
publications](https://ngff.openmicroscopy.org/publications/index.html) and the
[format
specification](https://ngff.openmicroscopy.org/specifications/index.html).
"""
    fp.write(ome_zarr_intro)

    open_scivis_intro = """
### Open SciVis Datasets

The [Open SciVis Datasets](https://klacansky.com/open-scivis-datasets/), curated
by Pavol Klacansky, is a valuable resource for the scientific visualization
community. This collection provides a diverse range of volumetric datasets that
are freely available for use in research, education, and development of
visualization techniques.

The datasets span various scientific domains, including medical imaging, fluid
dynamics, astrophysics, and materials science. Each dataset is provided in a
standardized format, typically raw binary files accompanied by metadata
describing dimensions, data types, and other relevant information.

One of the key benefits of this collection is that it offers high-quality,
real-world datasets that can be used to test and benchmark visualization
algorithms and software. This is particularly useful for researchers and
developers working on volume rendering, isosurface extraction, transfer function
design, and other visualization techniques.

The Open SciVis Datasets website provides easy access to download the datasets,
along with previews and descriptions of each dataset's contents and origins.
This makes it simple for users to find appropriate datasets for their specific
needs or interests.

By making these datasets freely available, Klacansky's collection promotes
reproducibility in scientific visualization research and enables fair
comparisons between different visualization methods using common benchmark data.
"""
    fp.write(open_scivis_intro)

    project_intro = """
### Project Overview

The OME-Zarr Open SciVis Datasets project is an innovative initiative that brings together two valuable resources for the scientific visualization community: the Open SciVis Datasets curated by Pavol Klacansky and the OME-Zarr file format developed by the Open Microscopy Environment.

This project takes the original Open SciVis Datasets and converts them into the OME-Zarr format, providing several key enhancements:

1. The datasets are restructured into a chunked, multi-scale form, allowing for efficient access to different resolutions and subsets of the data.

2. Metadata for each dataset is encoded in JSON format according to the OME-Zarr specification, providing standardized and machine-readable information about the data's structure and properties.

3. The converted datasets are hosted on Amazon Web Services (AWS) S3 through the AWS Open Data Program, ensuring wide accessibility and scalability.

The primary aim of the OME-Zarr Open SciVis Datasets project is to create a web-based resource that serves the scientific visualization community in multiple ways:

- It promotes reproducibility in research by providing standardized, easily accessible datasets that can be used as benchmarks or test cases across different studies.

- It offers a rich dataset resource for developers working on OME-Zarr tools, allowing them to test and refine their implementations using real-world scientific data.

- It demonstrates the capabilities of the OME-Zarr format in handling diverse types of scientific visualization data, from medical imaging to fluid dynamics simulations.

By combining the high-quality datasets from the Open SciVis collection with the advanced features of the OME-Zarr format, this project aims to accelerate progress in scientific visualization research and tool development while fostering greater interoperability and data sharing within the community.
"""
    fp.write(project_intro)

    fp.write("\n## Datasets\n")
    for dataset_name in get_dataset_names():
        dataset = get_dataset(dataset_name)
        fp.write(f"\n### {dataset_name}\n")
        thumbnail_path = f"./thumbnails/small/{dataset_name}.webp"
        if os.path.exists(thumbnail_path):
            fp.write(f"![{dataset_name}]({thumbnail_path})\n")
        else:
            print(f"Warning: No thumbnail found for {dataset_name}.")
        fp.write(f"\n> {dataset['description']}\n")
        fp.write(f"\n<details>\n<summary>Details</summary>\n\n")
        fp.write(f"**Dataset Name:** {dataset_name}\n\n")
        fp.write(f"**Dataset Type:** {dataset['type']}\n\n")
        fp.write(f"**Dataset Size:** {dataset['size']}\n\n")
        fp.write(f"**Dataset Spacing:** {dataset['spacing']}\n\n")

        s3_url = f"s3://ome-zarr-scivis/v0.5/96x2/{dataset_name}.ome.zarr"
        https_url = f"https://ome-zarr-scivis.s3.us-east-1.amazonaws.com/v0.5/96x2/{dataset_name}.ome.zarr"
        preview_url = f"https://kitware.github.io/itk-vtk-viewer/app/?image=https://ome-zarr-scivis.s3.us-east-1.amazonaws.com/v0.4/96x0/{dataset_name}.ome.zarr"
        structure_url = f"https://ome.github.io/ome-ngff-validator/?source=https://ome-zarr-scivis.s3.us-east-1.amazonaws.com/v0.5/96x0/{dataset_name}.ome.zarr"

        store = zarr.storage.FsspecStore.from_url(
            s3_url,
            read_only=True,
            storage_options={'anon':True}
        )
        multiscales = nz.from_ngff_zarr(store)
        scales = len(multiscales.images)
        fp.write(f"**Dataset Scales:** {scales}\n\n")
        fp.write(f"**Dataset HTTPS URL:** {https_url}\n\n")
        fp.write(f"**Dataset S3 URL:** {s3_url}\n\n")
        fp.write(f"**[Interactive visualization]({preview_url})**\n\n")
        fp.write(f"**[Interactive structure]({structure_url})**\n\n")
        fp.write(f"</details>\n")

    fp.write("\n### Sorted by number of voxels\n")
    def get_size(size_list):
        size = size_list[0] * size_list[1] * size_list[2]
        return size
    for idx, dataset_name in enumerate(sorted(get_dataset_names(), key=lambda x: get_size(get_dataset(x)['size']))):
        dataset = get_dataset(dataset_name)
        # add the size of the dataset to the end in scientific notation
        size_voxels = get_size(dataset['size'])
        size_voxels_scientific = f"{size_voxels:.1e}"
        fp.write(f"{idx+1}. [{dataset_name}](#{dataset_name}) - {size_voxels_scientific}\n")

    fp.write("\n### CT Scans\n")
    for dataset_name in get_dataset_names():
        dataset = get_dataset(dataset_name)
        if dataset["category"] == "CT":
            fp.write(f"- [{dataset_name}](#{dataset_name})\n")

    fp.write("\n### MRI Scans\n")
    for dataset_name in get_dataset_names():
        dataset = get_dataset(dataset_name)
        if dataset["category"] == "MRI":
            fp.write(f"- [{dataset_name}](#{dataset_name})\n")

    fp.write("\n### Microscopy Datasets\n")
    for dataset_name in get_dataset_names():
        dataset = get_dataset(dataset_name)
        if dataset["category"] == "Microscope":
            fp.write(f"- [{dataset_name}](#{dataset_name})\n")

    fp.write("\n### Simulation Datasets\n")
    for dataset_name in get_dataset_names():
        dataset = get_dataset(dataset_name)
        if dataset["category"] == "Simulation":
            fp.write(f"- [{dataset_name}](#{dataset_name})\n")

    fp.write("\n## Usage\n")
    usage_text = """
The OME-Zarr Open SciVis Datasets are freely available for download and use by the scientific visualization community.

### Python Loading Example

To load a dataset in Python, use the following example code:

```shell
pip install ngff-zarr s3fs matplotlib
```

```python
import ngff_zarr as nz
import zarr.storage
from rich import print
from matplotlib import pyplot as plt

store = zarr.storage.FsspecStore.from_url(
  's3://ome-zarr-scivis/v0.5/64x2/engine.ome.zarr',
  read_only=True,
  storage_options={'anon':True}
)
multiscales = nz.from_ngff_zarr(store)

print(multiscales)
```
------

```python
Multiscales(
    images=[
        NgffImage(
            data=dask.array<from-zarr, shape=(128, 256, 256), dtype=uint8, chunksize=(64, 64, 64), chunktype=numpy.ndarray>,
            dims=['z', 'y', 'x'],
            scale={'z': 1.0, 'y': 1.0, 'x': 1.0},
            translation={'z': -64.0, 'y': -128.0, 'x': -128.0},
            name='image',
            axes_units={'z': None, 'y': None, 'x': None},
            computed_callbacks=[]
        ),
        NgffImage(
            data=dask.array<from-zarr, shape=(128, 128, 128), dtype=uint8, chunksize=(64, 64, 64), chunktype=numpy.ndarray>,
            dims=['z', 'y', 'x'],
            scale={'z': 1.0, 'y': 2.0, 'x': 2.0},
            translation={'z': -64.0, 'y': -127.5, 'x': -127.5},
            name='image',
            axes_units={'z': None, 'y': None, 'x': None},
            computed_callbacks=[]
        )
    ],
    metadata=Metadata(
        axes=[Axis(name='z', type='space', unit=None), Axis(name='y', type='space', unit=None), Axis(name='x', type='space', unit=None)],
        datasets=[
            Dataset(
                path='scale0/engine',
                coordinateTransformations=[
                    Scale(scale=[1.0, 1.0, 1.0], type='scale'),
                    Translation(translation=[-64.0, -128.0, -128.0], type='translation')
                ]
            ),
            Dataset(
                path='scale1/engine',
                coordinateTransformations=[
                    Scale(scale=[1.0, 2.0, 2.0], type='scale'),
                    Translation(translation=[-64.0, -127.5, -127.5], type='translation')
                ]
            )
        ],
        coordinateTransformations=None,
        omero=None,
        name='image'
    ),
    scale_factors=None,
    method=None,
    chunks=None"
)
```

```python
plt.imshow(multiscales.images[1].data[64,:,:])
plt.show()
```

------

![Matplotlib engine rendering](./thumbnails/engine-matplotlib.png)

### Dataset Formats

#### version

All datasets are currently available in two OME-Zarr format versions,
Version 0.4 (Zarr 2-based), and Version 0.5 (Zarr 3-based).

- 0.4 : OME-Zarr Version 0.4
- 0.5 : OME-Zarr Version 0.5

#### chunks

Datasets are also available with different z,y,x chunk sizes.

- 64 : 64x64x64
- 96 : 96x96x96
- 128 : 128x128x28

#### shards

For the OME-Zarr v0.5, datasets, datasets are also available with different
sharding settings.

- 0 : 0x0x0 (no sharding)
- 2 : 2x2x2 (two chunks per shard in each dimension)
- 4 : 4x4x4

For OME-Zarr v0.4, only `0` (no sharding) is available.

#### URL format

The URL formats are:

- https://ome-zarr-scivis.s3.us-east-1.amazonaws.com/v{version}/{chunks}x{shards}/{dataset_name}.ome.zarr
- s3://ome-zarr-scivis/v{version}/{chunks}x{shards}/{dataset_name}.ome.zarr

"""
    fp.write(usage_text)

    fp.write("\n## License\n")
    license_text = """
The datasets in this collection are provided under various open licenses, including Creative Commons and public domain licenses. Please refer to the individual dataset descriptions for specific licensing information.

The OME-Zarr Open SciVis Datasets generation code is licensed under the [Apache 2.0 License](./LICENSE).
"""
    fp.write(license_text)

    fp.write("\n## Acknowledgements\n")
    acknowledgements_text = """
We would like to acknowledge the following individuals and organizations for their contributions and support:

- [Pavol Klacansky](https://klacansky.com/) for curating the original Open SciVis Datasets collection and making it freely available to the scientific visualization community.
- The [Open Microscopy Environment](https://www.openmicroscopy.org/) for developing the OME-Zarr file format and promoting open, collaborative standards for bioimaging data.
- [Amazon Web Services (AWS)](https://aws.amazon.com/) for hosting the OME-Zarr Open SciVis Datasets on the AWS S3 platform through the AWS Open Data Program.
- [NumFOCUS](https://numfocus.org/) for supporting the development and maintenance of open-source scientific computing tools and resources.
"""
    fp.write(acknowledgements_text)
