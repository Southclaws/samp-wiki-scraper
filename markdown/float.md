# float

## Description

Converts an integer into a float.

| Name  | Description                         |
| ----- | ----------------------------------- |
| value | Integer value to convert to a float |

## Returns

The given integer as a float

## Examples

```c
new Float:FloatValue;
new Value = 52;
FloatValue = float(Value);   // Converts Value(52) into a float and stores it in 'FloatValue' (52.0)
```

## Related Functions

- floatround: Convert a float to an integer (rounding).
- floatstr: Convert an string to a float.
