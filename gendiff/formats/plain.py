from gendiff.formats.stylish import out_root


def form(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def to_plain(diff, path=""):  # noqa C901
    lines = list()
    for element in diff:
        current_path = f'{path}{element["key"]}'
        if element["type"] == "add":
            lines.append(f"Property '{current_path}' "
                         f"was added with value: "
                         f"{form(element['new'])}")

        if element["type"] == "removed":
            lines.append(f"Property '{current_path}' was removed")

        if element["type"] == "changed":
            lines.append(f"Property '{current_path}'"
                         f" was updated. From {form(element['old'])} "
                         f"to {form(element['new'])}")

        if element["type"] == "nested":
            new_value = to_plain(element['children'], f"{current_path}.")
            lines.append(f"{new_value}")

    return "\n".join(lines)
