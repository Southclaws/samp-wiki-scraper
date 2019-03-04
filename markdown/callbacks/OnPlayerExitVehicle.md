---
title: OnPlayerExitVehicle
description: This callback is called when a player starts to exit a vehicle.
tags: ["player", "vehicle"]
---

# OnPlayerExitVehicle

<TagLinks />

## Description

This callback is called when a player starts to exit a vehicle.

| Name      | Description                                     |
| --------- | ----------------------------------------------- |
| playerid  | The ID of the player that is exiting a vehicle. |
| vehicleid | The ID of the vehicle the player is exiting.    |

## Returns

It is always called first in filterscripts.

## Examples

```c
public OnPlayerExitVehicle(playerid, vehicleid)
{
    new string[35];
    format(string, sizeof(string), "INFO: You are exiting vehicle %i", vehicleid);
    SendClientMessage(playerid, 0xFFFFFFFF, string);
    return 1;
}
```

## Notes

::: warning

Not called if the player falls off a bike or is removed from a vehicle by other means such as using SetPlayerPos.
You must use OnPlayerStateChange and check if their old state is PLAYER_STATE_DRIVER or PLAYER_STATE_PASSENGER and their new state is PLAYER_STATE_ONFOOT.

:::

## Related Functions

- RemovePlayerFromVehicle: Throw a player out of their vehicle.
- GetPlayerVehicleSeat: Check what seat a player is in.
