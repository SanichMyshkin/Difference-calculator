def diff_tree(first_data: dict, second_data: dict): # noqa C901
    diff = []

    db_dict = sorted(
        list(set(first_data.keys()) | set(second_data.keys()))
    )

    for key in db_dict:
        if key not in first_data:
            diff.append({
                "key": key,
                "operation": "add",
                "new": second_data[key]
            })
        elif key not in second_data:
            diff.append({
                "key": key,
                "operation": "removed",
                "old": first_data[key]
            })
        elif isinstance(first_data[key], dict) and \
                isinstance(second_data[key], dict):

            child = diff_tree(first_data[key], second_data[key])
            diff.append({
                "key": key,
                "operation": "nested",
                "value": child
            })
        elif first_data[key] == second_data[key]:
            diff.append({"key": key,
                         "operation": "same",
                         "value": first_data[key]})
        elif first_data[key] != second_data[key]:
            diff.append({"key": key,
                         "operation": "changed",
                         "old": first_data[key],
                         "new": second_data[key]})
    return diff
