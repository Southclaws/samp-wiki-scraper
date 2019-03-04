---
title: TextDrawHideForPlayer
description: Hides a textdraw for a specific player.
tags: ["player", "textdraw"]
---

# TextDrawHideForPlayer

<TagLinks />

## Description

Hides a textdraw for a specific player.

| Name     | Description                                                 |
| -------- | ----------------------------------------------------------- |
| playerid | The ID of the player that the textdraw should be hidden for |
| text     | The ID of the textdraw to hide                              |

## Returns

This function does not return any specific values.

## Examples

```c
new Text:Textdraw[MAX_PLAYERS];

public OnPlayerConnect(playerid)
{
    Textdraw[playerid] = TextDrawCreate( ... );
    return 1;
}

public OnPlayerDisconnect(playerid, reason)
{
    TextDrawDestroy(Textdraw[playerid]);
    return 1;
}

public OnPlayerSpawn(playerid)
{
    TextDrawShowForPlayer(playerid, Textdraw[playerid]);
    return 1;
}

public OnPlayerDeath(playerid, reason)
{
    TextDrawHideForPlayer(playerid, Textdraw[playerid]);
    return 1;
}
```

## Related Functions

- TextDrawHideForAll: Hide a textdraw for all players.
- TextDrawShowForPlayer: Show a textdraw for a certain player.
- TextDrawShowForAll: Show a textdraw for all players.
