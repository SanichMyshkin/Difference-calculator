def diff_tree(first_data: dict, second_data: dict):  # noqa C901
    diff = []

    db_dict = sorted(
        list(set(first_data.keys()) | set(second_data.keys()))
    )

    for key in db_dict:
        if key not in first_data:
            diff.append({
                "key": key,
                "type": "add",
                "new": second_data[key]
            })
        elif key not in second_data:
            diff.append({
                "key": key,
                "type": "removed",
                "old": first_data[key]
            })
        elif isinstance(first_data[key], dict) and \
                isinstance(second_data[key], dict):

            child = diff_tree(first_data[key], second_data[key])
            diff.append({
                "key": key,
                "type": "nested",
                "children": child
            })
        elif first_data[key] == second_data[key]:
            diff.append({"key": key,
                         "type": "same",
                         "value": first_data[key]})
        elif first_data[key] != second_data[key]:
            diff.append({"key": key,
                         "type": "changed",
                         "old": first_data[key],
                         "new": second_data[key]})
    return diff


def build(data1, data2):
    return dict(
        type='root',
        children=diff_tree(data1, data2),
    )


def out_root(item):
    if isinstance(item, dict):
        return item["children"]
    return item


def build_ident(sign: str):
    space = " "
    data_dict = {
        "add": "+",
        "removed": "-",
        "nothing": " "
    }
    return f'{space * 2}{data_dict[sign]}{space}'
