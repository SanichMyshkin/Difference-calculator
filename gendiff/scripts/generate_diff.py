import json

first_file = json.load(open('file1.json'))
second_file = json.load(open('file2.json'))


def run_generate_diff(first_file, second_file):
    print(parse_dict(generate_diff(first_file, second_file)))


def generate_diff(first_file, second_file):
    result = {}
    for key in first_file.keys():
        if key not in second_file.keys():
            result[f"- {key}"] = first_file[key]

        elif first_file[key] == second_file[key]:
            result[f"  {key}"] = second_file.pop(key)

        else:
            result[f"- {key}"] = first_file[key]

    result.update({f'+ {key}': item for key, item in second_file.items()})
    return result


def parse_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0][2:]))
    result = json.dumps(sorted_dict, indent=2).replace('"',"")
    return result


run_generate_diff(first_file, second_file)
