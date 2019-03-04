---
title: EditAttachedObject
description: Enter edition mode for an attached object.
tags: []
---

# EditAttachedObject

::: warning

This function was added in SA-MP 0.3e and will not work in earlier versions!

:::

## Description

Enter edition mode for an attached object.

| Name     | Description                                      |
| -------- | ------------------------------------------------ |
| playerid | The ID of the player to enter in to edition mode |
| index    | The index (slot) of the attached object to edit  |

## Returns

1 on success and 0 on failure.

## Examples

```c
public OnPlayerSpawn(playerid)
{
    SetPlayerAttachedObject(playerid, 0, 1337, 2);
}
 
public OnPlayerCommandText(playerid, cmdtext[])
{
    if(!strcmp(cmdtext, "/edit", true))
    {
        EditAttachedObject(playerid, 0);
        SendClientMessage(playerid, 0xFFFFFFFF, "SERVER: You now edit your attached object on index slot 0!");
        return 1;
    }
    return 0;
}
```

## Notes

::: tip

You can move the camera while editing by pressing and holding the spacebar (or W in vehicle) and moving your mouse.

:::

::: warning

Players will be able to scale objects up to a very large or negative value size. Limits should be put in place using OnPlayerEditAttachedObject to abort the edit.

:::

## Related Functions

- SetPlayerAttachedObject: Attach an object to a player
- RemovePlayerAttachedObject: Remove an attached object from a player
- IsPlayerAttachedObjectSlotUsed: Check whether an object is attached to a player in a specified index
- EditObject: Edit an object.
- EditPlayerObject: Edit an object.
- SelectObject: Select an object.
- CancelEdit: Cancel the edition of an object.
- OnPlayerEditAttachedObject: Called when a player finishes editing an attached object.
