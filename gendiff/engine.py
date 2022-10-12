from gendiff.parser import parse
from gendiff.difference import diff_tree
from gendiff.formats.stylish import stylish
from gendiff.formats.plain import plain


def generate_diff(first_file_path: str, second_file_path: str, formater="stylish"):  # noqa E501
    first_file = parse(first_file_path)
    second_file = parse(second_file_path)
    data_diff = diff_tree(first_file, second_file)
    if formater == "plain":
        return plain(data_diff)
    return stylish(data_diff)

# print(generate_diff('/home/udo/python-project-50/test/fixtures/tree_file1.yaml',
#                '/home/udo/python-project-50/test/fixtures/tree_file2.json'))
