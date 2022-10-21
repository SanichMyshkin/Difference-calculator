from gendiff.parser import get_data
from gendiff.difference import diff_tree, build
from gendiff.formatter import formatting


def generate_diff(first_file_path: str, second_file_path: str, formater="stylish"):  # noqa E501
    first_file = get_data(first_file_path)
    second_file = get_data(second_file_path)
    data_diff = diff_tree(first_file, second_file)
    return formatting(formater, data_diff)

# print(generate_diff("/home/udo/python-project-50//test/fixtures/tree_file1.yaml",
#                    "/home/udo/python-project-50//test/fixtures/tree_file2.json"))

# print(generate_diff("/home/udo/python-project-50//test/fixtures/tree_file1.yaml",
#                    "/home/udo/python-project-50//test/fixtures/tree_file2.json", formater="json"))
