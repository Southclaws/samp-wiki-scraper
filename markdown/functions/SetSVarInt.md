---
title: SetSVarInt
description: Set an integer server variable.
tags: []
---

# SetSVarInt

<TagLinks />

::: warning

This function was added in SA-MP 0.3.7 R2 and will not work in earlier versions!

:::

## Description

Set an integer server variable.

| Name      | Description                      |
| --------- | -------------------------------- |
| varname[] | The name of the server variable. |
| int_value | The integer to be set.           |

## Returns

1: The function executed successfully.

0: The function failed to execute. The variable name is null or over 40 characters.

## Examples

```c
// set "Version"
SetSVarInt("Version", 37);
// will print version that server has
printf("Version: %d", GetSVarInt("Version"));
```

## Related Functions

- GetSVarInt: Get a player server as an integer.
- SetSVarString: Set a string for a server variable.
- GetSVarString: Get the previously set string from a server variable.
- SetSVarFloat: Set a float for a server variable.
- GetSVarFloat: Get the previously set float from a server variable.
- DeleteSVar: Delete a server variable.
