#!/usr/bin/env python3

from sys import argv
from json import load


def to_markdown(obj):
    blocks = []

    if "name" not in obj:
        raise "missing 'name'"

    blocks.append(f'# {obj["name"]}')

    if obj["versions"] is not None:
        blocks.append(f'''::: warning

{obj["versions"]}

:::''')

    if obj["outdated"] is not None:
        blocks.append(f'''::: warning

{obj["outdated"]}

:::''')

    if obj["description"] is not None:
        blocks.append(f'''## Description

{obj["description"]}
''')

    if obj["params_body"] is not None:
        params_block = []
        params_block.append(f'| Name | Description |\n')
        params_block.append(f'|------|-------------|\n')
        for param in obj["params_body"]:
            params_block.append(f'|{param["name"]} | {param["description"]}|\n')
        blocks.append(''.join(params_block))

    if obj["return_values"] is not None:
        pass

    if obj["pawn_code"] is not None:
        pass

    if obj["code"] is not None:
        pass

    if obj["tips"] is not None:
        pass

    if obj["notes"] is not None:
        pass

    if obj["warnings"] is not None:
        pass

    if obj["related_fn"] is not None:
        pass

    if obj["related_cb"] is not None:
        pass

    return '\n\n'.join(blocks)

def main():
    if len(argv) != 2:
        print("Needs a file as argument.")
        return

    path = argv[1]
    output = ""
    with open(path) as fp:
        obj = load(fp)
        output = to_markdown(obj)

    print(output)


if __name__ == "__main__":
    main()
