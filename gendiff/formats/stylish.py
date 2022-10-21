from gendiff.difference import build_ident, out_root

STARTING_INDENT = 4


def nested(value, depth):
    if isinstance(value, dict):
        lines = ["{"]
        for key, nest_val in value.items():
            if isinstance(nest_val, dict):
                new_value = nested(nest_val, depth + STARTING_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nest_val}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return value


def form(dict, key, depth, sign):
    return f"{' ' * depth}{sign}{dict['key']}:" \
           f" {nested(dict[key], depth + STARTING_INDENT)}"


def to_stylish(diff, depth=0):  # noqa C901
    lines = ['{']
    diff = out_root(diff)
    for element in diff:
        if element["type"] == "same":
            lines.append(form(
                element, 'value',
                depth, build_ident("nothing")
            ))

        if element["type"] == "add":
            lines.append(form(
                element, "new",
                depth, build_ident("add")
            ))

        if element["type"] == "removed" or \
                element["type"] == "changed":
            lines.append(form(
                element, "old",
                depth, build_ident("removed")
            ))

        if element["type"] == "changed":
            lines.append(form(
                element, "new",
                depth, build_ident("add")
            ))

        if element["type"] == "nested":
            lines.append(f"{' ' * depth}    {element['key']}:"
                         f" {to_stylish(element['children'], depth + STARTING_INDENT)}")  # noqa E501

    lines.append(f'{" " * depth}}}')
    return "\n".join(lines)
