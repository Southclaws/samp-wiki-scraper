---
title: GetPlayerArmour
description: This function stores the armour of a player into a variable.
tags: ["player"]
---

# GetPlayerArmour

## Description

This function stores the armour of a player into a variable.

| Name          | Description                                               |
| ------------- | --------------------------------------------------------- |
| playerid      | The ID of the player that you want to get the armour of.  |
| &Float:armour | The float to to store the armour in, passed by reference. |

## Returns

1 - success

0 - failure (i.e. player not connected).

The player's armour is stored in the specified variable.

## Examples

```c
new Float:armour;
GetPlayerArmour(playerid, armour);
new s[40];
format(s, sizeof(s), "SERVER: Your armour is %0.f percent", armour);
SendClientMessage(playerid, 0xFFFFFFAA, s);
```

## Notes

::: warning

Even though the armour can be set to near infinite values on the server side, the individual clients will only report values up to 255. Anything higher will wrap around; 256 becomes 0, 257 becomes 1, etc.
Armour is obtained rounded to integers: set 50.15, but get 50.0

:::

## Related Functions

- SetPlayerArmour: Set the armour of a player.
- GetPlayerHealth: Find out how much health a player has.
- GetVehicleHealth: Check the health of a vehicle.
