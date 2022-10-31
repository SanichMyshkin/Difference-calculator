from gendiff.engine import generate_diff
import pytest
import os

tree_file1_yaml = os.path.join(os.path.dirname(__file__), 'fixtures', 'tree_file1.yaml')
tree_file2_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'tree_file2.json')

tree_answer = os.path.join(os.path.dirname(__file__), 'fixtures', 'answer_tree.txt')
tree_answer_palin = os.path.join(os.path.dirname(__file__), 'fixtures', 'answer_tree_plain.txt')
tree_answer_json = os.path.join(os.path.dirname(__file__), 'fixtures', 'answer_tree_json.txt')


def test_parse():
    with pytest.raises(Exception):
        generate_diff(tree_file1_yaml, "wrong_file")


def test_gendiff_tree():
    with open(tree_answer) as answer:
        assert generate_diff(tree_file1_yaml, tree_file2_json) == answer.read()


def test_gendiff_plain():
    with open(tree_answer_palin) as answer:
        assert generate_diff(tree_file1_yaml, tree_file2_json, formater="plain") == answer.read()


def test_gendiff_json():
    with open(tree_answer_json) as answer:
        assert generate_diff(tree_file1_yaml, tree_file2_json, formater="json") == answer.read()
