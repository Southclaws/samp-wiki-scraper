# TextDrawSetString

## Description

Changes the text on a textdraw.

| Name     | Description                     |
| -------- | ------------------------------- |
| text     | The TextDraw to change          |
| string[] | The new string for the TextDraw |

## Returns

This function does not return any specific values.

## Examples

```c
new Text:himessage;

public OnGameModeInit()
{
    himessage = TextDrawCreate(1.0, 5.6, "Hi, how are you?");
    return 1;
}

public OnPlayerConnect(playerid)
{
    new newtext[41], name[MAX_PLAYER_NAME];
    GetPlayerName(playerid, name, MAX_PLAYER_NAME);
    format(newtext, sizeof(newtext), "Hi %s, how are you?", name);
    TextDrawSetString(himessage, newtext);
    TextDrawShowForPlayer(playerid, himessage);
    return 1;
}
```

## Notes

::: warning

There are limits to the length of textdraw strings - see here for more info.

:::

## Related Functions

- TextDrawCreate: Create a textdraw.
- TextDrawDestroy: Destroy a textdraw.
- TextDrawColor: Set the color of the text in a textdraw.
- TextDrawBoxColor: Set the color of the box in a textdraw.
- TextDrawBackgroundColor: Set the background color of a textdraw.
- TextDrawAlignment: Set the alignment of a textdraw.
- TextDrawFont: Set the font of a textdraw.
- TextDrawLetterSize: Set the letter size of the text in a textdraw.
- TextDrawTextSize: Set the size of a textdraw box.
- TextDrawSetOutline: Choose whether the text has an outline.
- TextDrawSetShadow: Toggle shadows on a textdraw.
- TextDrawSetProportional: Scale the text spacing in a textdraw to a proportional ratio.
- TextDrawUseBox: Toggle if the textdraw has a box or not.
- TextDrawShowForPlayer: Show a textdraw for a certain player.
- TextDrawHideForPlayer: Hide a textdraw for a certain player.
- TextDrawShowForAll: Show a textdraw for all players.
- TextDrawHideForAll: Hide a textdraw for all players.
