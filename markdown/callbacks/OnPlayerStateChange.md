---
title: OnPlayerStateChange
description: This callback is called when a player changes state.
tags: ["player"]
---

# OnPlayerStateChange

<TagLinks />

## Description

This callback is called when a player changes state. For example, when a player changes from being the driver of a vehicle to being on-foot.

| Name     | Description                              |
| -------- | ---------------------------------------- |
| playerid | The ID of the player that changed state. |
| newstate | The player's new state.                  |
| oldstate | The player's previous state.             |

## Returns

It is always called first in filterscripts.

## Examples

```c
public OnPlayerStateChange(playerid, newstate, oldstate)
{
    if(oldstate == PLAYER_STATE_ONFOOT && newstate == PLAYER_STATE_DRIVER) // Player entered a vehicle as a driver
    {
        new vehicleid = GetPlayerVehicleID(playerid);
        AddVehicleComponent(vehicleid, 1010); // Add NOS to the vehicle
    }
    return 1;
}
```

## Notes

::: tip

This callback can also be called by NPC.

:::

## Related Functions

- GetPlayerState: Get a player's current state.
- GetPlayerSpecialAction: Get a player's current special action.
- SetPlayerSpecialAction: Set a player's special action.
