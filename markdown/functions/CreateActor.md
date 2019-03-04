---
title: CreateActor
description: Create a static 'actor' in the world.
tags: []
---

# CreateActor

<TagLinks />

::: warning

This function was added in SA-MP 0.3.7 and will not work in earlier versions!

:::

## Description

Create a static 'actor' in the world. These 'actors' are like NPCs, however they have limited functionality. They do not take up server player slots.

| Name     | Description                                        |
| -------- | -------------------------------------------------- |
| modelid  | The model ID (skin ID) the actor should have.      |
| x        | The X coordinate to create the actor at.           |
| y        | The Y coordinate to create the actor at.           |
| z        | The Z coordinate to create the actor at.           |
| Rotation | The facing angle (rotation) for the actor to have. |

## Returns

The created Actor ID (start at 0).

INVALID_ACTOR_ID (65535) If the actor limit (1000) is reached.

## Examples

```c
new ActorCJ;

public OnGameModeInit()
{
    // Create an actor (CJ) at Blueberry Acres (Center of SA map)
    ActorCJ = CreateActor(0, 0.0, 0.0, 3.0, 0.0);
}
```

## Notes

::: tip

Actors are designed to just stand somewhere, for example cashiers and bartenders. They can perform animations (once or looping) using ApplyActorAnimation.

:::

::: warning

Actors are completely separate from NPCs. They do NOT use player IDs/slots on the server and CANNOT be handled like NPCs.
Actors are limited to 1000 (MAX_ACTORS).
Actors can be pushed by vehicles, use a timer to put them back at their positions.
As of 0.3.7 R2 actors default to being invulnerable.

:::

## Related Functions

- DestroyActor: Destroy an actor.
- SetActorPos: Set the position of an actor.
- GetActorPos: Get the position of an actor.
- SetActorFacingAngle: Set the facing angle of an actor.
- GetActorFacingAngle: Get the facing angle of an actor.
- SetActorVirtualWorld: Set the virtual world of an actor.
- GetActorVirtualWorld: Get the virtual world of an actor.
- ApplyActorAnimation: Apply an animation to an actor.
- ClearActorAnimations: Clear any animations that are applied to an actor.
- GetPlayerCameraTargetActor: Get the ID of the actor (if any) a player is looking at.
- IsActorStreamedIn: Checks if an actor is streamed in for a player.
- SetActorHealth: Set the health of an actor.
- GetActorHealth: Gets the health of an actor.
- SetActorInvulnerable: Set actor invulnerable.
- IsActorInvulnerable: Check if actor is invulnerable.
- IsValidActor: Check if actor id is valid.
- GetActorPoolSize: Gets the highest actorid created on the server.
- GetPlayerTargetActor: Gets id of an actor which is aimed by certain player.
- OnActorStreamIn: Called when an actor is streamed in by a player.
- OnActorStreamOut: Called when an actor is streamed out by a player.
- OnPlayerGiveDamageActor: This callback is called when a player gives damage to an actor.
