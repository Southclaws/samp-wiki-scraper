---
title: GetObjectPos
description: Get the position of an object.
tags: []
---

# GetObjectPos

<TagLinks />

## Description

Get the position of an object.

| Name     | Description                                                         |
| -------- | ------------------------------------------------------------------- |
| objectid | The ID of the object to get the position of..                       |
| &Float:X | A variable in which to store the X coordinate, passed by reference. |
| &Float:Y | A variable in which to store the Y coordinate, passed by reference. |
| &Float:Z | A variable in which to store the Z coordinate, passed by reference. |

## Returns

1: The function executed successfully.

0: The function failed to execute. The specified object does not exist.

## Examples

```c
new Float:x, Float:y, Float:z;
GetObjectPos(objectid, x, y, z);
```

## Related Functions

- CreateObject: Create an object.
- DestroyObject: Destroy an object.
- IsValidObject: Checks if a certain object is vaild.
- MoveObject: Move an object.
- StopObject: Stop an object from moving.
- SetObjectPos: Set the position of an object.
- SetObjectRot: Set the rotation of an object.
- GetObjectRot: Check the rotation of an object.
- AttachObjectToPlayer: Attach an object to a player.
- CreatePlayerObject: Create an object for only one player.
- DestroyPlayerObject: Destroy a player object.
- IsValidPlayerObject: Checks if a certain player object is vaild.
- MovePlayerObject: Move a player object.
- StopPlayerObject: Stop a player object from moving.
- SetPlayerObjectPos: Set the position of a player object.
- SetPlayerObjectRot: Set the rotation of a player object.
- GetPlayerObjectPos: Locate a player object.
- GetPlayerObjectRot: Check the rotation of a player object.
- AttachPlayerObjectToPlayer: Attach a player object to a player.
