---
title: StopPlayerHoldingObject
description: Removes attached objects.
tags: ["player"]
---

# StopPlayerHoldingObject

<TagLinks />

::: warning

This function was added in SA-MP 0.3b and will not work in earlier versions!

:::

## Description

Removes attached objects.

| Name     | Description                                          |
| -------- | ---------------------------------------------------- |
| playerid | ID of the player you want to remove the object from. |

## Returns

1 on success, 0 on failure

## Examples

```c
public OnPlayerDeath(playerid, killerid, reason)
{
    if(IsPlayerHoldingObject(playerid)) StopPlayerHoldingObject(playerid);
    return 1;
}
```

## Notes

::: warning

This function was removed in SA-MP 0.3c. check RemovePlayerAttachedObject

:::

## Related Functions
