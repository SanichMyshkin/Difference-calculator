from gendiff.engine import generate_diff
from gendiff.parser import parse
import pytest

file1_json = 'test/fixtures/flat_file1.json'
file2_yaml = 'test/fixtures/flat_file2.yaml'

tree_file1_yaml = 'test/fixtures/tree_file1.yaml'
tree_file2_json = 'test/fixtures/tree_file2.json'


def test_parse():
    with pytest.raises(Exception):
        generate_diff('test/fixtures/flat_file1.json', 'test/fixtures/file2.wrong')


def test_generate_diff():
    with open('test/fixtures/answer_flat.txt') as answer:
        assert generate_diff(file1_json, file2_yaml) == answer.read()


def test_gendiff_tree():
    with open('test/fixtures/answer_tree.txt') as answer:
        assert generate_diff(tree_file1_yaml, tree_file2_json) == answer.read()
    # Тесты пока что не проходят, так как я не допили функцию