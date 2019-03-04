---
title: OnFilterScriptInit
description: This callback is called when a filterscript is initialized (loaded).
tags: []
---

# OnFilterScriptInit

<TagLinks />

## Description

This callback is called when a filterscript is initialized (loaded). It is only called inside the filterscript which is starting.

| Name | Description |
| ---- | ----------- |


## Examples

```c
public OnFilterScriptInit()
{
    print("\n--------------------------------------");
    print("The filterscript is loaded.");
    print("--------------------------------------\n");
    return 1;
}
```

## Related Functions
