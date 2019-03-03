# AttachObjectToVehicle

::: warning

This function was added in SA-MP 0.3c and will not work in earlier versions!

:::

## Description

Attach an object to a vehicle.

| Name          | Description                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| objectid      | The ID of the object to attach to the vehicle. Note that this is an object ID, not a model ID. The object must be CreateObject created first. |
| vehicleid     | The ID of the vehicle to attach the object to.                                                                                                |
| Float:OffsetX | The X axis offset from the vehicle to attach the object to.                                                                                   |
| Float:OffsetY | The Y axis offset from the vehicle to attach the object to.                                                                                   |
| Float:OffsetZ | The Z axis offset from the vehicle to attach the object to.                                                                                   |
| Float:RotX    | The X rotation offset for the object.                                                                                                         |
| Float:RotY    | The Y rotation offset for the object.                                                                                                         |
| Float:RotZ    | The Z rotation offset for the object.                                                                                                         |

## Returns

This function does not return any specific values.

## Examples

```c
new objectid = CreateObject(...);
new vehicleid = GetPlayerVehicleID(playerid);
AttachObjectToVehicle(objectid, vehicleid, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0);
```

## Notes

::: tip

The object must be created first.

:::

::: warning

When the vehicle is destroyed or respawned, the attached objects won't be destroyed with it; they will remain stationary at the position the vehicle disappeared and be reattached to the next vehicle to claim the vehicle ID that the objects were attached to.

:::

## Related Functions

- AttachObjectToPlayer: Attach an object to a player.
- AttachObjectToObject: Attach an object to an object.
- AttachPlayerObjectToPlayer: Attach a player object to a player.
- CreateObject: Create an object.
- DestroyObject: Destroy an object.
- IsValidObject: Checks if a certain object is vaild.
- MoveObject: Move an object.
- StopObject: Stop an object from moving.
- SetObjectPos: Set the position of an object.
- SetObjectRot: Set the rotation of an object.
- GetObjectPos: Locate an object.
- GetObjectRot: Check the rotation of an object.
- CreatePlayerObject: Create an object for only one player.
- DestroyPlayerObject: Destroy a player object.
- IsValidPlayerObject: Checks if a certain player object is vaild.
- MovePlayerObject: Move a player object.
- StopPlayerObject: Stop a player object from moving.
- SetPlayerObjectPos: Set the position of a player object.
- SetPlayerObjectRot: Set the rotation of a player object.
- GetPlayerObjectPos: Locate a player object.
- GetPlayerObjectRot: Check the rotation of a player object.
