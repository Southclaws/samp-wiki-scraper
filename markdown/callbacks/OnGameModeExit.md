---
title: OnGameModeExit
description: This callback is called when a gamemode ends, either through 'gmx', the server being shut down, or GameModeExit.
tags: []
---

# OnGameModeExit

<TagLinks />

## Description

This callback is called when a gamemode ends, either through 'gmx', the server being shut down, or GameModeExit.

| Name | Description |
| ---- | ----------- |


## Examples

```c
public OnGameModeExit()
{
    print("Gamemode ended.");
    return 1;
}
```

## Notes

::: tip

This function can also be used in a filterscript to detect if the gamemode changes with RCON commands like changemode or gmx, as changing the gamemode does not reload a filterscript.
When using OnGameModeExit in conjunction with the 'rcon gmx' console command keep in mind there is a potential for client bugs to occur an example of this is excessive RemoveBuildingForPlayer calls during OnGameModeInit which could result in a client crash.
This callback will NOT be called if the server crashes or the process is killed by other means, such as using the Linux kill command or pressing the close-button on the Windows console.

:::

## Related Functions

- GameModeExit: Exit the current gamemode.
