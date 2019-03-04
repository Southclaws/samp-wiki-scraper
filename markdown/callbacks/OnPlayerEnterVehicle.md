---
title: OnPlayerEnterVehicle
description: This callback is called when a player starts to enter a vehicle, meaning the player is not in vehicle yet at the time this callback is called.
tags: ["player", "vehicle"]
---

# OnPlayerEnterVehicle

<TagLinks />

## Description

This callback is called when a player starts to enter a vehicle, meaning the player is not in vehicle yet at the time this callback is called.

| Name        | Description                                          |
| ----------- | ---------------------------------------------------- |
| playerid    | ID of the player who attempts to enter a vehicle.    |
| vehicleid   | ID of the vehicle the player is attempting to enter. |
| ispassenger | 0 if entering as driver. 1 if entering as passenger. |

## Returns

It is always called first in filterscripts.

## Examples

```c
public OnPlayerEnterVehicle(playerid, vehicleid, ispassenger)
{
    new string[128];
    format(string, sizeof(string), "You are entering vehicle %i", vehicleid);
    SendClientMessage(playerid, 0xFFFFFFFF, string);
    return 1;
}
```

## Notes

::: tip

This callback is called when a player BEGINS to enter a vehicle, not when they HAVE entered it. See OnPlayerStateChange.
This callback is still called if the player is denied entry to the vehicle (e.g. it is locked or full).

:::

## Related Functions

- PutPlayerInVehicle: Put a player in a vehicle.
- GetPlayerVehicleSeat: Check what seat a player is in.
