import json
import yaml
from yaml.loader import SafeLoader
import os


def parse(file_path):
    filename, format = os.path.splitext(os.path.normpath(file_path))
    with open(file_path) as file:
        if format.lower == ".json":
            return json.load(file)
        elif format.lower == ".yaml" or ".yml":
            return yaml.load(file, Loader=SafeLoader)
