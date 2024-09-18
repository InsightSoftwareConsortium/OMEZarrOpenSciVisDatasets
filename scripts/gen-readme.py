#!/usr/bin/env python3

import os
import re
import sys
import json

def get_datasets_json():
    input_datasets_json="data/open-scivis-datasets/datasets.json"
    with open(input_datasets_json, "r") as f:
        datasets = json.load(f)
    return datasets

DATASETS = get_datasets_json()
def get_datasets():
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
        fp.write(f"**Dataset URL:** {dataset['url']}\n\n")
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
The OME-Zarr Open SciVis Datasets are freely available for download and use by the scientific visualization community. To access the datasets, follow these steps:
# todo after uploading to S3
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
