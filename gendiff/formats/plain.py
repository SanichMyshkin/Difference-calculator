from gendiff.difference import diff_tree
from gendiff.parser import parse

fdata1 = parse("/home/udo/python-project-50/test/fixtures/tree_file1.yaml")
fdata2 = parse("/home/udo/python-project-50/test/fixtures/tree_file1.yaml")

db = diff_tree(fdata1, fdata2)

print(db)


def plain():


# x = diff_tree()
