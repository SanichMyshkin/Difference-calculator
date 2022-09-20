import json


def run_generate_diff(first_file_path: str, second_file_path: str) -> str:
    first_file = json.load(open(first_file_path))
    second_file = json.load(open(second_file_path))
    gendiff = generate_diff(first_file, second_file)
    print(parse_dict(gendiff))


def generate_diff(first_file, second_file):
    result = dict()
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
    result = json.dumps(sorted_dict, indent=2).replace('"', "")
    return result

# c30716bf386f7d64f64aa6be72917e70df7f54dcde8e640ff9e73db935fc89b7
