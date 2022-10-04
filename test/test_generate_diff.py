from gendiff.engine import generate_diff
from gendiff.parser import parse
import pytest

file1_json = 'test/fixtures/file1.json'
file2_yaml = 'test/fixtures/file2.yaml'


def test_parse():
    with pytest.raises(Exception):
        generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.wrong')


def test_generate_diff():
    with open('test/fixtures/answer_json.txt') as answer:
        assert generate_diff(file1_json, file2_yaml) == answer.read()

# print(gendiff("/home/udo/python-project-50/test/fixtures/file1.json","/home/udo/python-project-50/test/fixtures/file2.yaml"))
