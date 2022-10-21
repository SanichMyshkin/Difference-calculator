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
    """
    Я не совсем понимаю зачем мы создали функцию build, что бы
    потом избавляться от корня. С точки зрения полной картины задумка хорошая,
    но я столкнулся с тем что to_stylish рекурсивно вызывает функцию в которой используют
    листы, а build возвращает словарь. Обходит таким способом - diff["children"] в начале
    функции не выходи, так как при последующем вызове передавать КЛЮЧ в СЛОВАРЬ нельзя и
    выходит что мы передаем индекс, а он строка, но никак не число. Поэтому я наколхозил
    функцию для выхода из корня дерева. Однако в другом формате та же песня, реализовывать ее там
    смысла нет, поскольку это же дублирование кода - нужно делать функцию, но как на мой взгляд
    это усложняет логистику в проекте.
    """
    if isinstance(item, dict):
        item["children"]
    return item


def build_ident(sign: str):
    space = " "
    data_dict = {
        "add": "+",
        "removed": "-",
        "nothing": " "
    }
    return f'{space * 2}{data_dict[sign]}{space}'
