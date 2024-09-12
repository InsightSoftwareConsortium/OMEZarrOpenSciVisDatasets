import json

input_datasets_json="data/open-scivis-datasets/datasets.json"
output_datsets_json="data/ome-zarr-open-scivis-datasets/datasets.json"

with open(input_datasets_json, "r") as f:
    datasets = json.load(f)

new_datasets = {}

for dataset_name in datasets:
    dataset = datasets[dataset_name]
    dataset.pop("type")
    dataset.pop("size")
    dataset.pop("spacing")
    dataset.pop("sha512sum")
    dataset.pop("url")
    new_datasets[dataset_name] = dataset

with open(output_datsets_json, "w") as f:
    json.dump(new_datasets, f, indent=4)
