# GameTextForPlayer

## Description

Shows 'game text' (on-screen text) for a certain length of time for a specific player.

| Name           | Description                                           |
| -------------- | ----------------------------------------------------- |
| playerid       | The ID of the player to show the gametext for.        |
| const string[] | The text to be displayed.                             |
| time           | The duration of the text being shown in milliseconds. |
| style          | The style of text to be displayed.                    |

## Returns

1: The function executed successfully. Success is reported when the style and/or time is invalid. Nothing will happen though (no text displayed). May also cause game crashes.

0: The function failed to execute. This means either the string is null or the player is not connected.

## Examples

```c
public OnPlayerDeath(playerid, killerid, reason)
{
    GameTextForPlayer(playerid, "Wasted", 5000, 2);
    return 1;
}
```

## Related Functions

- GameTextForAll: Display gametext to all players.
- TextDrawShowForPlayer: Show a textdraw for a certain player.
