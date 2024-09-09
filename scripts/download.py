#!/usr/bin/env python3

"""Download the current open-scivis-datasets."""

from pathlib import Path
import hashlib

import httpx
from rich import print
from rich.progress import Progress
import numpy as np

data_dir = Path(__file__).parent.parent / "data" / "open-scivis-datasets"
datasets_json_url = "https://klacansky.com/open-scivis-datasets/datasets.json"
max_size = 30 * 1024 ** 3  # 30 GB

if not data_dir.exists():
    data_dir.mkdir(parents=True)

# download the datasets.json file with httpx and save it to the data directory, load the json file contents
with httpx.Client() as client:
    response = client.get(datasets_json_url)
    response.raise_for_status()
    with open(data_dir / "datasets.json", "wb") as f:
        f.write(response.content)
    datasets = response.json()

# download all the datasets listed in the datasets.json file less than max_size
for dataset_name in datasets:
    dataset = datasets[dataset_name]
    dtype = np.dtype(dataset["type"])
    component_size = dtype.itemsize
    size_xyz = dataset["size"]
    size_bytes = size_xyz[0] * size_xyz[1] * size_xyz[2] * component_size
    if size_bytes < max_size:
        url = dataset["url"]
        output_file = data_dir / "/".join(url.split("/")[-2:])
        print(f"Downloading {dataset['name']} to {output_file}...")
        output_file.parent.mkdir(parents=True, exist_ok=True)

        if output_file.exists():
            print(f"File {output_file} already exists, skipping download.")
        else:
            with httpx.stream("GET", url) as response:
                with open(output_file, "wb") as f:
                    for chunk in response.iter_bytes():
                        f.write(chunk)
        sha512sum = dataset["sha512sum"]
        print(f"Verifying {output_file}...")
        with open(output_file, "rb") as f:
            data = f.read()
        if sha512sum != hashlib.sha512(data).hexdigest():
            print(f"Error: {output_file} failed checksum verification.")
            output_file.unlink()
        else:
            print(f"Success: {output_file} passed checksum verification.")