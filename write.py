#!/usr/bin/env python3

from sys import argv
from json import load


def clean_description(s):
    return s.split(".", 1)[0].replace(":", "") + "."


def to_markdown(obj):
    blocks = []

    if "name" not in obj:
        raise "missing 'name'"
    if "description" not in obj:
        raise "missing 'description'"

    blocks.append(f'''---
title: {obj["name"]}
description: {clean_description(obj["description"])}
tags: {obj["tags"]}
---''')

    blocks.append(f'# {obj["name"]}')

    blocks.append(f'<TagLinks />')

    if obj["versions"] is not None:
        blocks.append(f'''::: warning

{obj["versions"]}

:::''')

    if obj["outdated"] is not None:
        blocks.append(f'''::: warning

{obj["outdated"]}

:::''')

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
        blocks.append(f'''## Returns

{obj["return_values"]}
''')

    if len(obj["pawn_code"]) > 0 or len(obj["code"]) > 0:
        newline = "\n"
        blocks.append("## Examples\n")
        if len(obj["pawn_code"]) > 0:
            blocks.append(f'''```c
{newline.join(obj["pawn_code"])}
```
''')

        if len(obj["code"]) > 0:
            blocks.append(f'''```
{newline.join(obj["code"])}
```
''')

    if obj["tips"] is not None or obj["notes"] is not None or obj["warnings"] is not None:
        blocks.append("## Notes")

        if obj["notes"] is not None:
            blocks.append(f'''::: tip

{obj["notes"]}

:::
''')

        if obj["tips"] is not None:
            blocks.append(f'''::: tip

{obj["tips"]}

:::
''')

        if obj["warnings"] is not None:
            blocks.append(f'''::: warning

{obj["warnings"]}

:::
''')

    if obj["related_fn"] is not None:
        blocks.append("## Related Functions\n")
        newline = "\n"
        related = []
        for fn in obj["related_fn"]:
            related.append(f"- {fn.strip(newline)}")
        blocks.append('\n'.join(related))

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
