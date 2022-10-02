import json


def generate_diff(first_file_path, second_file_path):
    first_file = json.load(open(first_file_path))
    second_file = json.load(open(second_file_path))

    result = dict()
    for key in first_file.keys():
        if key not in second_file.keys():
            result[f"- {key}"] = first_file[key]

        elif first_file[key] == second_file[key]:
            result[f"  {key}"] = second_file.pop(key)

        else:
            result[f"- {key}"] = first_file[key]

    result.update({f'+ {key}': item for key, item in second_file.items()})
    sorted_dict = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    return json.dumps(sorted_dict, indent=2).replace('"', "").replace(",", "")


print(generate_diff("/home/udo/python-project-50/test/fixtures/file1.json",
                   "/home/udo/python-project-50/test/fixtures/file2.json"))
