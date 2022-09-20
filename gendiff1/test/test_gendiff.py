from gendiff1.engine import generate_diff, parse_dict

answer_gen = {'- 1': '1', '  second': '2', '- third': '3', '+ first': '1', '+ third': 3}  # noqa E501
answer_pars = "{\n  - 1: 1,\n  + first: 1,\n    second: 2,\n  - third: 3,\n  + third: 3\n}"  # noqa E501


def test_generate():
    res_gen = generate_diff({1: "1",
                             "second": "2",
                             "third": "3"},

                            {"first": "1",
                             "second": "2",
                             "third": 3})
    assert res_gen == answer_gen


def test_parse():
    assert parse_dict(answer_gen) == answer_pars
