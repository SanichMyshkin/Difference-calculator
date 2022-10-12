from gendiff.parser import parse
from gendiff.difference import diff_tree
from gendiff.formats.stylish import to_stylish
from gendiff.formats.plain import to_plain
from gendiff.formats.to_json import to_json


def generate_diff(first_file_path: str, second_file_path: str, formater="stylish"):  # noqa E501
    first_file = parse(first_file_path)
    second_file = parse(second_file_path)
    data_diff = diff_tree(first_file, second_file)
    if formater == "plain":
        return to_plain(data_diff)
    if formater == "json":
        return to_json(data_diff)
    return to_stylish(data_diff)
