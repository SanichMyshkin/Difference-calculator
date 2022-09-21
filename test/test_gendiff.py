from gendiff.engine import generate_diff, parse_dict

answer_gen = {'- 1': '1', '  second': '2', '- third': '3', '+ first': '1', '+ third': 3}  # noqa E501
answer_gen1 = {'- True': False, '- False': True, '- 1.3': 12, '+ True': 'False', '+ False': True}  # noqa E501
answer_pars = "{\n  - 1: 1,\n  + first: 1,\n    second: 2,\n  - third: 3,\n  + third: 3\n}"  # noqa E501


# заменить ответы и перенести в файл

def test_generate():
    assert generate_diff({1: "1",
                          "second": "2",
                          "third": "3"},

                         {"first": "1",
                          "second": "2",
                          "third": 3}) == answer_gen
    assert generate_diff({
        "True": False,
        False: True,
        1.3: 12},
        {
            True: "False",
            "False": True
        }) == {'- True': False, '- False': True, '- 1.3': 12, '+ True': 'False', '+ False': True}

    def test_parse():
        assert parse_dict(answer_gen) == answer_pars
        assert parse_dict(
            answer_gen1) == "{\n  - True: False,\n  - False: True,\n  - 1.3: 12,\n  + True: False,\n  + False: True\n}"  # noqa E501
