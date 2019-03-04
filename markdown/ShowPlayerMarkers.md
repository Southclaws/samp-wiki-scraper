---
title: ShowPlayerMarkers
description: Toggles player markers (blips on the radar).
tags: ["player"]
---

# ShowPlayerMarkers

## Description

Toggles player markers (blips on the radar). Must be used when the server starts (OnGameModeInit). For other times, see SetPlayerMarkerForPlayer.

| Name | Description                                                                                                          |
| ---- | -------------------------------------------------------------------------------------------------------------------- |
| mode | The mode to use for markers. They can be streamed, meaning they are only visible to nearby players. See table below. |

## Returns

This function does not return any specific values.

## Examples

```c
public OnGameModeInit()
{
    // Player markers only visible to nearby players
    ShowPlayerMarkers(PLAYER_MARKERS_MODE_STREAMED);
}
```

## Notes

::: tip

It is also possible to set a player's color to a color that has full transparency (no alpha value). This makes it possible to show markers on a per-player basis.

:::

## Related Functions

- SetPlayerMarkerForPlayer: Set a player's marker.
- LimitPlayerMarkerRadius: Limit the player marker radius.
- ShowNameTags: Set nametags on or off.
- SetPlayerColor: Set a player's color.
