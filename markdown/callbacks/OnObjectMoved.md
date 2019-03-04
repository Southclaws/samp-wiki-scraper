---
title: OnObjectMoved
description: This callback is called when an object is moved after MoveObject (when it stops moving).
tags: []
---

# OnObjectMoved

<TagLinks />

## Description

This callback is called when an object is moved after MoveObject (when it stops moving).

| Name     | Description                         |
| -------- | ----------------------------------- |
| objectid | The ID of the object that was moved |

## Returns

It is always called first in filterscripts.

## Examples

```c
public OnObjectMoved(objectid)
{
    printf("Object %d finished moving.",objectid);
    return 1;
}
```

## Notes

::: tip

SetObjectPos does not work when used in this callback. To fix it, recreate the object.

:::

## Related Functions

- MoveObject: Move an object.
- MovePlayerObject: Move a player object.
- IsObjectMoving: Check if the object is moving.
- StopObject: Stop an object from moving.
- OnPlayerObjectMoved: Called when a player-object stops moving.
