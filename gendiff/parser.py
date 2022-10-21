import json
import yaml
import os


def get_data(file_path):
    filename, format = os.path.splitext(os.path.normpath(file_path))
    with open(file_path) as file:
        return parse(file, format)


def parse(data, format):
    if format == ".json":
        return json.load(data)
    if format == ".yaml" or ".yml":
        return yaml.safe_load(data)
    raise ValueError(f"{format} - format not supported")
