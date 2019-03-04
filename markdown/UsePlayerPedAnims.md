---
title: UsePlayerPedAnims
description: Uses standard player walking animation (animation of the CJ skin) instead of custom animations for every skin (e.
tags: ["player"]
---

# UsePlayerPedAnims

## Description

Uses standard player walking animation (animation of the CJ skin) instead of custom animations for every skin (e.g. skating for skater skins).

| Name | Description |
| ---- | ----------- |


## Examples

```c
public OnGameModeInit()
{
    UsePlayerPedAnims();
    return 1;
}
```

## Notes

::: tip

Only works when placed under OnGameModeInit.
Not using this function causes two-handed weapons (not dual-handed - a single weapon that is held by both hands) to be held in only one hand.

:::

## Related Functions

- ApplyAnimation: Apply an animation to a player.
- ClearAnimations: Clear any animations a player is performing.
