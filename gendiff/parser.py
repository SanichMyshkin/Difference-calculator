import json
import yaml
import os


def parse(file_path):
    filename, format = os.path.splitext(os.path.normpath(file_path))
    with open(file_path) as file:
        if format.lower == ".json":
            return json.load(file)
        if format.lower == ".yaml" or ".yml":
            return yaml.safe_load(file)
