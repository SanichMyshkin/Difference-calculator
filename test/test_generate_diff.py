from gendiff.engine import generate_diff

file1_json = 'test/fixtures/file1.json'
file2_json = 'test/fixtures/file2.json'


def test_generate_diff():
    with open('test/fixtures/answer_json.txt', "r") as answer:
        assert generate_diff(file1_json, file2_json) == answer.read()

# print(gendiff("/home/udo/python-project-50/test/fixtures/file1.json","/home/udo/python-project-50/test/fixtures/file2.json"))
