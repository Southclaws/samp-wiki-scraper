---
title: OnPlayerInteriorChange
description: Called when a player changes interior.
tags: ["player"]
---

# OnPlayerInteriorChange

<TagLinks />

## Description

Called when a player changes interior. Can be triggered by SetPlayerInterior or when a player enter/exits a building.

| Name          | Description                            |
| ------------- | -------------------------------------- |
| playerid      | The playerid who changed interior.     |
| newinteriorid | The interior the player is now in.     |
| oldinteriorid | The interior the player was in before. |

## Returns

It is always called first in gamemode.

## Examples

```c
public OnPlayerInteriorChange(playerid, newinteriorid, oldinteriorid)
{
    new string[42];
    format(string, sizeof(string), "You went from interior %d to interior %d!", oldinteriorid, newinteriorid);
    SendClientMessage(playerid, COLOR_ORANGE, string);
    return 1;
}
```

## Related Functions

- SetPlayerInterior: Set a player's interior.
- GetPlayerInterior: Get the current interior of a player.
- LinkVehicleToInterior: Change the interior that a vehicle is seen in.
- OnPlayerStateChange: Called when a player changes state.
