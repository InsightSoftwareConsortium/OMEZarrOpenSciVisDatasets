# OME-Zarr Open SciVis Datasets

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

## Datasets

### 3d_neurons_15_sept_2016
![3d_neurons_15_sept_2016](./thumbnails/small/3d_neurons_15_sept_2016.webp)

> The neurons are macaque visual cortical neurons labeled with TdTomato fluorescent proteins.

<details>
<summary>Details</summary>

**Dataset Name:** 3d_neurons_15_sept_2016

**Dataset Type:** uint16

**Dataset Size:** [2048, 2048, 1718]

**Dataset Spacing:** [0.267345, 0.267345, 0.5]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/3d_neurons_15_sept_2016/3d_neurons_15_sept_2016_2048x2048x1718_uint16.raw

</details>

### aneurism
![aneurism](./thumbnails/small/aneurism.webp)

> Rotational C-arm x-ray scan of the arteries of the right half of a human head. A contrast agent was injected into the blood and an aneurism is present.

<details>
<summary>Details</summary>

**Dataset Name:** aneurism

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 256]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/aneurism/aneurism_256x256x256_uint8.raw

</details>

### backpack
![backpack](./thumbnails/small/backpack.webp)

> CT scan of a backpack filled with items.

<details>
<summary>Details</summary>

**Dataset Name:** backpack

**Dataset Type:** uint16

**Dataset Size:** [512, 512, 373]

**Dataset Spacing:** [0.9766, 0.9766, 1.25]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/backpack/backpack_512x512x373_uint16.raw

</details>

### beechnut
![beechnut](./thumbnails/small/beechnut.webp)

> A microCT scan of a dried beechnut.

<details>
<summary>Details</summary>

**Dataset Name:** beechnut

**Dataset Type:** uint16

**Dataset Size:** [1024, 1024, 1546]

**Dataset Spacing:** [2e-05, 2e-05, 2e-05]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/beechnut/beechnut_1024x1024x1546_uint16.raw

</details>

### blunt_fin
![blunt_fin](./thumbnails/small/blunt_fin.webp)

> 

<details>
<summary>Details</summary>

**Dataset Name:** blunt_fin

**Dataset Type:** uint8

**Dataset Size:** [256, 128, 64]

**Dataset Spacing:** [1, 0.75, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/blunt_fin/blunt_fin_256x128x64_uint8.raw

</details>

### bonsai
![bonsai](./thumbnails/small/bonsai.webp)

> CT scan of a bonsai tree.

<details>
<summary>Details</summary>

**Dataset Name:** bonsai

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 256]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/bonsai/bonsai_256x256x256_uint8.raw

</details>

### boston_teapot
![boston_teapot](./thumbnails/small/boston_teapot.webp)

> CT scan of the SIGGRAPH 1989 teapot with a small version of the AVS lobster inside.

<details>
<summary>Details</summary>

**Dataset Name:** boston_teapot

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 178]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/boston_teapot/boston_teapot_256x256x178_uint8.raw

</details>

### bunny
![bunny](./thumbnails/small/bunny.webp)

> A CT scan of the Stanford Bunny. The greyscale units are Hounsfield units, denoting electron-density of the subject; the scale units are in millimeters. The scan was completed 28 January 2000.

<details>
<summary>Details</summary>

**Dataset Name:** bunny

**Dataset Type:** uint16

**Dataset Size:** [512, 512, 361]

**Dataset Spacing:** [0.337891, 0.337891, 0.5]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/bunny/bunny_512x512x361_uint16.raw

</details>

### carp
![carp](./thumbnails/small/carp.webp)

> CT scan of a carp fish

<details>
<summary>Details</summary>

**Dataset Name:** carp

**Dataset Type:** uint16

**Dataset Size:** [256, 256, 512]

**Dataset Spacing:** [0.78125, 0.390625, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/carp/carp_256x256x512_uint16.raw

</details>

### chameleon
![chameleon](./thumbnails/small/chameleon.webp)

> CT scan of a chameleon.

<details>
<summary>Details</summary>

**Dataset Name:** chameleon

**Dataset Type:** uint16

**Dataset Size:** [1024, 1024, 1080]

**Dataset Spacing:** [0.09228515625, 0.09228515625, 0.105]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/chameleon/chameleon_1024x1024x1080_uint16.raw

</details>

### christmas_tree
![christmas_tree](./thumbnails/small/christmas_tree.webp)

> The Christmas tree model was scanned with a Siemens Somatom Plus 4 Volume Zoom Multislice-CT scanner at the general hospital in Vienna.

<details>
<summary>Details</summary>

**Dataset Name:** christmas_tree

**Dataset Type:** uint16

**Dataset Size:** [512, 499, 512]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/christmas_tree/christmas_tree_512x499x512_uint16.raw

</details>

### csafe_heptane
![csafe_heptane](./thumbnails/small/csafe_heptane.webp)

> A single time step from a computational simulation of a jet of heptane gas undergoing combustion.

<details>
<summary>Details</summary>

**Dataset Name:** csafe_heptane

**Dataset Type:** uint8

**Dataset Size:** [302, 302, 302]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/csafe_heptane/csafe_heptane_302x302x302_uint8.raw

</details>

### dns

> A pressure field of a direct numerical simulation of fully developed flow at different Reynolds numbers in a plane channel have been performed with POONGBACK code which uses the spectral numerical method of Kim, Moin and Moser (J. Fluid Mech. vol 177, page 133).

<details>
<summary>Details</summary>

**Dataset Name:** dns

**Dataset Type:** float64

**Dataset Size:** [10240, 7680, 1536]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/dns/dns_10240x7680x1536_float64.raw

</details>

### duct
![duct](./thumbnails/small/duct.webp)

> A wall-bounded flow in a duct.

<details>
<summary>Details</summary>

**Dataset Name:** duct

**Dataset Type:** float32

**Dataset Size:** [193, 194, 1000]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/duct/duct_193x194x1000_float32.raw

</details>

### engine
![engine](./thumbnails/small/engine.webp)

> CT scan of two cylinders of an engine block.

<details>
<summary>Details</summary>

**Dataset Name:** engine

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 128]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/engine/engine_256x256x128_uint8.raw

</details>

### foot
![foot](./thumbnails/small/foot.webp)

> Rotational C-arm x-ray scan of a human foot. Tissue and bone are present in the dataset.

<details>
<summary>Details</summary>

**Dataset Name:** foot

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 256]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/foot/foot_256x256x256_uint8.raw

</details>

### frog
![frog](./thumbnails/small/frog.webp)

> MRI scan of a frog as part of the Whole Frog Project.

<details>
<summary>Details</summary>

**Dataset Name:** frog

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 44]

**Dataset Spacing:** [0.5, 0.5, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/frog/frog_256x256x44_uint8.raw

</details>

### fuel
![fuel](./thumbnails/small/fuel.webp)

> Simulation of fuel injection into a combustion chamber. The higher the density value, the less presence of air.

<details>
<summary>Details</summary>

**Dataset Name:** fuel

**Dataset Type:** uint8

**Dataset Size:** [64, 64, 64]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/fuel/fuel_64x64x64_uint8.raw

</details>

### hcci_oh
![hcci_oh](./thumbnails/small/hcci_oh.webp)

> The first timestep of direct numerical simulation of an autoignition phenomena in stratified dimethyl-ether/air turbulent mixtures.

<details>
<summary>Details</summary>

**Dataset Name:** hcci_oh

**Dataset Type:** float32

**Dataset Size:** [560, 560, 560]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/hcci_oh/hcci_oh_560x560x560_float32.raw

</details>

### hydrogen_atom
![hydrogen_atom](./thumbnails/small/hydrogen_atom.webp)

> Simulation of the spatial probability distribution of the electron in an hydrogen atom, residing in a strong magnetic field.

<details>
<summary>Details</summary>

**Dataset Name:** hydrogen_atom

**Dataset Type:** uint8

**Dataset Size:** [128, 128, 128]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/hydrogen_atom/hydrogen_atom_128x128x128_uint8.raw

</details>

### isotropic_pressure

> Pressure field of a direct numerical simulation of forced isotropic turbulence.

<details>
<summary>Details</summary>

**Dataset Name:** isotropic_pressure

**Dataset Type:** float32

**Dataset Size:** [4096, 4096, 4096]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/isotropic_pressure/isotropic_pressure_4096x4096x4096_float32.raw

</details>

### jicf_q
![jicf_q](./thumbnails/small/jicf_q.webp)

> Q-criterion of a jet in crossflow created by a direct numerical simulation.

<details>
<summary>Details</summary>

**Dataset Name:** jicf_q

**Dataset Type:** float32

**Dataset Size:** [1408, 1080, 1100]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/jicf_q/jicf_q_1408x1080x1100_float32.raw

</details>

### kingsnake
![kingsnake](./thumbnails/small/kingsnake.webp)

> Scan of a Lampropeltis getula egg (captive bred by Travis LaDuc; laid on 7 July 2003, growth terminated on 29 August 2003, 54 days after oviposition) for Dr. Timothy Rowe of the Department of Geological Sciences, The University of Texas at Austin.

<details>
<summary>Details</summary>

**Dataset Name:** kingsnake

**Dataset Type:** uint8

**Dataset Size:** [1024, 1024, 795]

**Dataset Spacing:** [0.03174, 0.03174, 0.0688]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/kingsnake/kingsnake_1024x1024x795_uint8.raw

</details>

### lobster
![lobster](./thumbnails/small/lobster.webp)

> CT scan of a lobster contained in a block of resin.

<details>
<summary>Details</summary>

**Dataset Name:** lobster

**Dataset Type:** uint8

**Dataset Size:** [301, 324, 56]

**Dataset Spacing:** [1, 1, 1.4]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/lobster/lobster_301x324x56_uint8.raw

</details>

### magnetic_reconnection
![magnetic_reconnection](./thumbnails/small/magnetic_reconnection.webp)

> A single time step from a computational simulation of magnetic reconnection.

<details>
<summary>Details</summary>

**Dataset Name:** magnetic_reconnection

**Dataset Type:** float32

**Dataset Size:** [512, 512, 512]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/magnetic_reconnection/magnetic_reconnection_512x512x512_float32.raw

</details>

### marmoset_neurons
![marmoset_neurons](./thumbnails/small/marmoset_neurons.webp)

> Pyramidal neurons in the marmoset primary visual cortex (V1) labeled with green fluorescent protein (GFP) after injection of a psuedotyped G-deleted rabies virus in area V2. The tissue was cleared using the Sca/e technique and imaged on a Olympus 2-photon microscope at 20x magnification.

<details>
<summary>Details</summary>

**Dataset Name:** marmoset_neurons

**Dataset Type:** uint8

**Dataset Size:** [1024, 1024, 314]

**Dataset Spacing:** [0.497, 0.497, 1.5]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/marmoset_neurons/marmoset_neurons_1024x1024x314_uint8.raw

</details>

### marschner_lobb
![marschner_lobb](./thumbnails/small/marschner_lobb.webp)

> High frequencies where 99% of the sinusoids are right below the Nyquist frequency.

<details>
<summary>Details</summary>

**Dataset Name:** marschner_lobb

**Dataset Type:** uint8

**Dataset Size:** [41, 41, 41]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/marschner_lobb/marschner_lobb_41x41x41_uint8.raw

</details>

### miranda
![miranda](./thumbnails/small/miranda.webp)

> A time step of a density field in a simulation of the mixing transition in Rayleigh-Taylor instability.

<details>
<summary>Details</summary>

**Dataset Name:** miranda

**Dataset Type:** float32

**Dataset Size:** [1024, 1024, 1024]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/miranda/miranda_1024x1024x1024_float32.raw

</details>

### mri_ventricles
![mri_ventricles](./thumbnails/small/mri_ventricles.webp)

> 1.5T MRT 3D CISS dataset of a human head that highlights the CSF (Cerebro-Spinal-Fluid) filled cavities of the head.

<details>
<summary>Details</summary>

**Dataset Name:** mri_ventricles

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 124]

**Dataset Spacing:** [0.9, 0.9, 0.9]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/mri_ventricles/mri_ventricles_256x256x124_uint8.raw

</details>

### mri_woman
![mri_woman](./thumbnails/small/mri_woman.webp)

> MRI scan of a woman's head

<details>
<summary>Details</summary>

**Dataset Name:** mri_woman

**Dataset Type:** uint16

**Dataset Size:** [256, 256, 109]

**Dataset Spacing:** [1, 1, 1.5]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/mri_woman/mri_woman_256x256x109_uint16.raw

</details>

### mrt_angio
![mrt_angio](./thumbnails/small/mrt_angio.webp)

> 3T MRT Time-of-Flight Angiography dataset of a human head. The dataset has been resampled into an isotropic voxel grid (hence the peculiar slice size).

<details>
<summary>Details</summary>

**Dataset Name:** mrt_angio

**Dataset Type:** uint16

**Dataset Size:** [416, 512, 112]

**Dataset Spacing:** [0.412, 0.412, 0.412]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/mrt_angio/mrt_angio_416x512x112_uint16.raw

</details>

### neghip
![neghip](./thumbnails/small/neghip.webp)

> Simulation of the spatial probability distribution of the electrons in a high potential protein molecule.

<details>
<summary>Details</summary>

**Dataset Name:** neghip

**Dataset Type:** uint8

**Dataset Size:** [64, 64, 64]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/neghip/neghip_64x64x64_uint8.raw

</details>

### neocortical_layer_1_axons
![neocortical_layer_1_axons](./thumbnails/small/neocortical_layer_1_axons.webp)

> Axons in layer 1 of the mouse barrel cortex imaged in vivo.

<details>
<summary>Details</summary>

**Dataset Name:** neocortical_layer_1_axons

**Dataset Type:** uint8

**Dataset Size:** [1464, 1033, 76]

**Dataset Spacing:** [1, 1, 3.4]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/neocortical_layer_1_axons/neocortical_layer_1_axons_1464x1033x76_uint8.raw

</details>

### nucleon
![nucleon](./thumbnails/small/nucleon.webp)

> Simulation of the two-body distribution probability of a nucleon in the atomic nucleus 16O if a second nucleon is known to be positioned at r'=(2 fm,0,0).

<details>
<summary>Details</summary>

**Dataset Name:** nucleon

**Dataset Type:** uint8

**Dataset Size:** [41, 41, 41]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/nucleon/nucleon_41x41x41_uint8.raw

</details>

### pancreas
![pancreas](./thumbnails/small/pancreas.webp)

> First scan. The National Institutes of Health Clinical Center performed 82 abdominal contrast enhanced 3D CT scans (~70 seconds after intravenous contrast injection in portal-venous) from 53 male and 27 female subjects. Seventeen of the subjects are healthy kidney donors scanned prior to nephrectomy. The remaining 65 patients were selected by a radiologist from patients who neither had major abdominal pathologies nor pancreatic cancer lesions. Subjects' ages range from 18 to 76 years with a mean age of 46.8 ± 16.7. The CT scans have resolutions of 512x512 pixels with varying pixel sizes and slice thickness between 1.5 - 2.5 mm, acquired on Philips and Siemens MDCT scanners (120 kVp tube voltage). A medical student manually performed slice-by-slice segmentations of the pancreas as ground-truth and these were verified/modified by an experienced radiologist.

<details>
<summary>Details</summary>

**Dataset Name:** pancreas

**Dataset Type:** int16

**Dataset Size:** [240, 512, 512]

**Dataset Spacing:** [1.16, 1.0, 1.0]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/pancreas/pancreas_240x512x512_int16.raw

</details>

### pawpawsaurus
![pawpawsaurus](./thumbnails/small/pawpawsaurus.webp)

> This specimen, the holotype, was collected from the Paw Paw Formation, SMU Loc. No. 263, Tarrant County, Texas. The specimen was scanned along the coronal axis for a total of 1088 slices. Voxel size is 0.2275 mm.

<details>
<summary>Details</summary>

**Dataset Name:** pawpawsaurus

**Dataset Type:** uint16

**Dataset Size:** [958, 646, 1088]

**Dataset Spacing:** [0.2275, 0.2275, 0.2275]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/pawpawsaurus/pawpawsaurus_958x646x1088_uint16.raw

</details>

### pig_heart
![pig_heart](./thumbnails/small/pig_heart.webp)

> Volumes were obtained by way of computed tomography (CT) imaging on excised, postmortem porcine hearts. Alginate curing agents were injected into ventricles to provide rigidity and radiopaque agents were injected into the coronary arteries to distinguish microvasculature from the rest of the tissue.

<details>
<summary>Details</summary>

**Dataset Name:** pig_heart

**Dataset Type:** int16

**Dataset Size:** [2048, 2048, 2612]

**Dataset Spacing:** [0.03557, 0.03557, 0.03557]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/pig_heart/pig_heart_2048x2048x2612_int16.raw

</details>

### present
![present](./thumbnails/small/present.webp)

> An industrial CT scan of a christmas present.

<details>
<summary>Details</summary>

**Dataset Name:** present

**Dataset Type:** uint16

**Dataset Size:** [492, 492, 442]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/present/present_492x492x442_uint16.raw

</details>

### prone
![prone](./thumbnails/small/prone.webp)

> CT scan of abdomen in prone orientation (back faces ceiling, belly faces table).

<details>
<summary>Details</summary>

**Dataset Name:** prone

**Dataset Type:** uint16

**Dataset Size:** [512, 512, 463]

**Dataset Spacing:** [0.625, 0.625, 1.0]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/prone/prone_512x512x463_uint16.raw

</details>

### richtmyer_meshkov
![richtmyer_meshkov](./thumbnails/small/richtmyer_meshkov.webp)

> Entropy field (timestep 160) of Richtmyer-Meshkov instability simulation.

<details>
<summary>Details</summary>

**Dataset Name:** richtmyer_meshkov

**Dataset Type:** uint8

**Dataset Size:** [2048, 2048, 1920]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/richtmyer_meshkov/richtmyer_meshkov_2048x2048x1920_uint8.raw

</details>

### rotstrat_temperature

> Temperature field of a direct numerical simulation of rotating stratified turbulence.

<details>
<summary>Details</summary>

**Dataset Name:** rotstrat_temperature

**Dataset Type:** float32

**Dataset Size:** [4096, 4096, 4096]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/rotstrat_temperature/rotstrat_temperature_4096x4096x4096_float32.raw

</details>

### shockwave
![shockwave](./thumbnails/small/shockwave.webp)

> Simulation of an unsteady interaction of a planar shockwave with a randomly-perturbed contact discontinuity.

<details>
<summary>Details</summary>

**Dataset Name:** shockwave

**Dataset Type:** uint8

**Dataset Size:** [64, 64, 512]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/shockwave/shockwave_64x64x512_uint8.raw

</details>

### silicium
![silicium](./thumbnails/small/silicium.webp)

> Simulation of a silicium grid.

<details>
<summary>Details</summary>

**Dataset Name:** silicium

**Dataset Type:** uint8

**Dataset Size:** [98, 34, 34]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/silicium/silicium_98x34x34_uint8.raw

</details>

### skull
![skull](./thumbnails/small/skull.webp)

> Rotational C-arm x-ray scan of phantom of a human skull.

<details>
<summary>Details</summary>

**Dataset Name:** skull

**Dataset Type:** uint8

**Dataset Size:** [256, 256, 256]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/skull/skull_256x256x256_uint8.raw

</details>

### spathorhynchus
![spathorhynchus](./thumbnails/small/spathorhynchus.webp)

> This specimen, the holotype, was collected from the Middle Eocene Green River Formation of Sweetwater County, Wyoming on 27 July 1967 by Frank L. Pearce. The specimen was scanned along the coronal axis for a total of 750 slices. Each 1024x1024 pixel slice is 0.047 mm thick, with an interslice spacing of 0.047 mm and a field of reconstruction of 22 mm.

<details>
<summary>Details</summary>

**Dataset Name:** spathorhynchus

**Dataset Type:** uint16

**Dataset Size:** [1024, 1024, 750]

**Dataset Spacing:** [0.0215, 0.0215, 0.047]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/spathorhynchus/spathorhynchus_1024x1024x750_uint16.raw

</details>

### stag_beetle
![stag_beetle](./thumbnails/small/stag_beetle.webp)

> The stag beetle from Georg Glaeser, Vienna University of Applied Arts, Austria, was scanned with an industrial CT by Johannes Kastner, Wels College of Engineering, Austria, and Meister Eduard Gröller, Vienna University of Technology, Austria.

<details>
<summary>Details</summary>

**Dataset Name:** stag_beetle

**Dataset Type:** uint16

**Dataset Size:** [832, 832, 494]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/stag_beetle/stag_beetle_832x832x494_uint16.raw

</details>

### statue_leg
![statue_leg](./thumbnails/small/statue_leg.webp)

> CT scan of a leg of a bronze statue.

<details>
<summary>Details</summary>

**Dataset Name:** statue_leg

**Dataset Type:** uint8

**Dataset Size:** [341, 341, 93]

**Dataset Spacing:** [1, 1, 4]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/statue_leg/statue_leg_341x341x93_uint8.raw

</details>

### stent
![stent](./thumbnails/small/stent.webp)

> CT Scan of the abdomen and pelvis. The dataset contains also a stent in the abdominal aorta. No contrast agent was used to enhance the blood vessels.

<details>
<summary>Details</summary>

**Dataset Name:** stent

**Dataset Type:** uint16

**Dataset Size:** [512, 512, 174]

**Dataset Spacing:** [0.8398, 0.8398, 3.2]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/stent/stent_512x512x174_uint16.raw

</details>

### synthetic_truss_with_five_defects
![synthetic_truss_with_five_defects](./thumbnails/small/synthetic_truss_with_five_defects.webp)

> A simulated CT scan of a 8x8x8 octet truss with five defects on the front side of the object. The defects are bent strut, broken strut, missing strut, dross, and thin strut.

<details>
<summary>Details</summary>

**Dataset Name:** synthetic_truss_with_five_defects

**Dataset Type:** float32

**Dataset Size:** [1200, 1200, 1200]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/synthetic_truss_with_five_defects/synthetic_truss_with_five_defects_1200x1200x1200_float32.raw

</details>

### tacc_turbulence
![tacc_turbulence](./thumbnails/small/tacc_turbulence.webp)

> The dataset represents a time step from an isotropic turbulence simulation. A single variable, enstrophy, is represented on a Cartesian grid.

<details>
<summary>Details</summary>

**Dataset Name:** tacc_turbulence

**Dataset Type:** float32

**Dataset Size:** [256, 256, 256]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/tacc_turbulence/tacc_turbulence_256x256x256_float32.raw

</details>

### tooth
![tooth](./thumbnails/small/tooth.webp)

> 

<details>
<summary>Details</summary>

**Dataset Name:** tooth

**Dataset Type:** uint8

**Dataset Size:** [103, 94, 161]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/tooth/tooth_103x94x161_uint8.raw

</details>

### vertebra
![vertebra](./thumbnails/small/vertebra.webp)

> Rotational angiography scan of a head with an aneurysm. Only contrasted blood vessels are visible.

<details>
<summary>Details</summary>

**Dataset Name:** vertebra

**Dataset Type:** uint16

**Dataset Size:** [512, 512, 512]

**Dataset Spacing:** [0.1953, 0.1953, 0.1953]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/vertebra/vertebra_512x512x512_uint16.raw

</details>

### vis_male
![vis_male](./thumbnails/small/vis_male.webp)

> Male head scan

<details>
<summary>Details</summary>

**Dataset Name:** vis_male

**Dataset Type:** uint8

**Dataset Size:** [128, 256, 256]

**Dataset Spacing:** [1.57774, 0.995861, 1.00797]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/vis_male/vis_male_128x256x256_uint8.raw

</details>

### woodbranch
![woodbranch](./thumbnails/small/woodbranch.webp)

> A microCT scan of dried wood branch (hazelnut).

<details>
<summary>Details</summary>

**Dataset Name:** woodbranch

**Dataset Type:** uint16

**Dataset Size:** [2048, 2048, 2048]

**Dataset Spacing:** [1.8e-05, 1.8e-05, 1.8e-05]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/woodbranch/woodbranch_2048x2048x2048_uint16.raw

</details>

### zeiss
![zeiss](./thumbnails/small/zeiss.webp)

> Car part reconstructed from projections.

<details>
<summary>Details</summary>

**Dataset Name:** zeiss

**Dataset Type:** uint8

**Dataset Size:** [680, 680, 680]

**Dataset Spacing:** [1, 1, 1]

**Dataset URL:** https://klacansky.com/open-scivis-datasets/zeiss/zeiss_680x680x680_uint8.raw

</details>

### Sorted by number of voxels
1. [marschner_lobb](#marschner_lobb) - 6.9e+04
2. [nucleon](#nucleon) - 6.9e+04
3. [silicium](#silicium) - 1.1e+05
4. [fuel](#fuel) - 2.6e+05
5. [neghip](#neghip) - 2.6e+05
6. [tooth](#tooth) - 1.6e+06
7. [blunt_fin](#blunt_fin) - 2.1e+06
8. [hydrogen_atom](#hydrogen_atom) - 2.1e+06
9. [shockwave](#shockwave) - 2.1e+06
10. [frog](#frog) - 2.9e+06
11. [lobster](#lobster) - 5.5e+06
12. [mri_woman](#mri_woman) - 7.1e+06
13. [mri_ventricles](#mri_ventricles) - 8.1e+06
14. [engine](#engine) - 8.4e+06
15. [vis_male](#vis_male) - 8.4e+06
16. [statue_leg](#statue_leg) - 1.1e+07
17. [boston_teapot](#boston_teapot) - 1.2e+07
18. [aneurism](#aneurism) - 1.7e+07
19. [bonsai](#bonsai) - 1.7e+07
20. [foot](#foot) - 1.7e+07
21. [skull](#skull) - 1.7e+07
22. [tacc_turbulence](#tacc_turbulence) - 1.7e+07
23. [mrt_angio](#mrt_angio) - 2.4e+07
24. [csafe_heptane](#csafe_heptane) - 2.8e+07
25. [carp](#carp) - 3.4e+07
26. [duct](#duct) - 3.7e+07
27. [stent](#stent) - 4.6e+07
28. [pancreas](#pancreas) - 6.3e+07
29. [bunny](#bunny) - 9.5e+07
30. [backpack](#backpack) - 9.8e+07
31. [present](#present) - 1.1e+08
32. [neocortical_layer_1_axons](#neocortical_layer_1_axons) - 1.1e+08
33. [prone](#prone) - 1.2e+08
34. [christmas_tree](#christmas_tree) - 1.3e+08
35. [magnetic_reconnection](#magnetic_reconnection) - 1.3e+08
36. [vertebra](#vertebra) - 1.3e+08
37. [hcci_oh](#hcci_oh) - 1.8e+08
38. [zeiss](#zeiss) - 3.1e+08
39. [marmoset_neurons](#marmoset_neurons) - 3.3e+08
40. [stag_beetle](#stag_beetle) - 3.4e+08
41. [pawpawsaurus](#pawpawsaurus) - 6.7e+08
42. [spathorhynchus](#spathorhynchus) - 7.9e+08
43. [kingsnake](#kingsnake) - 8.3e+08
44. [miranda](#miranda) - 1.1e+09
45. [chameleon](#chameleon) - 1.1e+09
46. [beechnut](#beechnut) - 1.6e+09
47. [jicf_q](#jicf_q) - 1.7e+09
48. [synthetic_truss_with_five_defects](#synthetic_truss_with_five_defects) - 1.7e+09
49. [3d_neurons_15_sept_2016](#3d_neurons_15_sept_2016) - 7.2e+09
50. [richtmyer_meshkov](#richtmyer_meshkov) - 8.1e+09
51. [woodbranch](#woodbranch) - 8.6e+09
52. [pig_heart](#pig_heart) - 1.1e+10
53. [isotropic_pressure](#isotropic_pressure) - 6.9e+10
54. [rotstrat_temperature](#rotstrat_temperature) - 6.9e+10
55. [dns](#dns) - 1.2e+11

### CT Scans
- [aneurism](#aneurism)
- [backpack](#backpack)
- [beechnut](#beechnut)
- [bonsai](#bonsai)
- [boston_teapot](#boston_teapot)
- [bunny](#bunny)
- [carp](#carp)
- [chameleon](#chameleon)
- [christmas_tree](#christmas_tree)
- [engine](#engine)
- [foot](#foot)
- [kingsnake](#kingsnake)
- [lobster](#lobster)
- [mrt_angio](#mrt_angio)
- [pancreas](#pancreas)
- [pawpawsaurus](#pawpawsaurus)
- [pig_heart](#pig_heart)
- [present](#present)
- [prone](#prone)
- [skull](#skull)
- [spathorhynchus](#spathorhynchus)
- [stag_beetle](#stag_beetle)
- [statue_leg](#statue_leg)
- [stent](#stent)
- [synthetic_truss_with_five_defects](#synthetic_truss_with_five_defects)
- [vertebra](#vertebra)
- [vis_male](#vis_male)
- [woodbranch](#woodbranch)
- [zeiss](#zeiss)

### MRI Scans
- [frog](#frog)
- [mri_ventricles](#mri_ventricles)
- [mri_woman](#mri_woman)

### Microscopy Datasets
- [3d_neurons_15_sept_2016](#3d_neurons_15_sept_2016)
- [marmoset_neurons](#marmoset_neurons)
- [neocortical_layer_1_axons](#neocortical_layer_1_axons)

### Simulation Datasets
- [blunt_fin](#blunt_fin)
- [csafe_heptane](#csafe_heptane)
- [dns](#dns)
- [duct](#duct)
- [fuel](#fuel)
- [hcci_oh](#hcci_oh)
- [hydrogen_atom](#hydrogen_atom)
- [isotropic_pressure](#isotropic_pressure)
- [jicf_q](#jicf_q)
- [magnetic_reconnection](#magnetic_reconnection)
- [marschner_lobb](#marschner_lobb)
- [miranda](#miranda)
- [neghip](#neghip)
- [nucleon](#nucleon)
- [richtmyer_meshkov](#richtmyer_meshkov)
- [rotstrat_temperature](#rotstrat_temperature)
- [shockwave](#shockwave)
- [silicium](#silicium)
- [tacc_turbulence](#tacc_turbulence)

## Usage

The OME-Zarr Open SciVis Datasets are freely available for download and use by the scientific visualization community. To access the datasets, follow these steps:
# todo after uploading to S3

## License

The datasets in this collection are provided under various open licenses, including Creative Commons and public domain licenses. Please refer to the individual dataset descriptions for specific licensing information.

The OME-Zarr Open SciVis Datasets generation code is licensed under the [Apache 2.0 License](./LICENSE).

## Acknowledgements

We would like to acknowledge the following individuals and organizations for their contributions and support:

- [Pavol Klacansky](https://klacansky.com/) for curating the original Open SciVis Datasets collection and making it freely available to the scientific visualization community.
- The [Open Microscopy Environment](https://www.openmicroscopy.org/) for developing the OME-Zarr file format and promoting open, collaborative standards for bioimaging data.
- [Amazon Web Services (AWS)](https://aws.amazon.com/) for hosting the OME-Zarr Open SciVis Datasets on the AWS S3 platform through the AWS Open Data Program.
- [NumFOCUS](https://numfocus.org/) for supporting the development and maintenance of open-source scientific computing tools and resources.
