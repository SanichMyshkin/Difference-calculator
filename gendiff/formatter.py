from gendiff.formats.stylish import to_stylish
from gendiff.formats.plain import to_plain
from gendiff.formats.to_json import to_json


def formatting(format_name, tree):
    if format_name == "plain":
        return to_plain(tree)
    elif format_name == "json":
        return to_json(tree)
    else:
        return to_stylish(tree)
