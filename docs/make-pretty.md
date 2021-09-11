# Making pretty text

## Classes

The `ansiscape.strings` package contains a number of classes to help make your text beautiful.

### Text colour

- `Black()`
- `Blue()`
- `Cyan()`
- `Green()`
- `Magenta()`
- `Red()`
- `White()`
- `Yellow()`
- `BrightBlack()`
- `BrightBlue()`
- `BrightCyan()`
- `BrightGreen()`
- `BrightMagenta()`
- `BrightRed()`
- `BrightWhite()`
- `BrightYellow()`

### Background colour

- `BlackBackground()`
- `BlueBackground()`
- `CyanBackground()`
- `GreenBackground()`
- `MagentaBackground()`
- `RedBackground()`
- `WhiteBackground()`
- `YellowBackground()`
- `BrightBlackBackground()`
- `BrightBlueBackground()`
- `BrightCyanBackground()`
- `BrightGreenBackground()`
- `BrightMagentaBackground()`
- `BrightRedBackground()`
- `BrightWhiteBackground()`
- `BrightYellowBackground()`

### Alternate fonts

- `AlternativeFont0()`
- `AlternativeFont1()`
- `AlternativeFont2()`
- `AlternativeFont3()`
- `AlternativeFont4()`
- `AlternativeFont5()`
- `AlternativeFont6()`
- `AlternativeFont7()`
- `AlternativeFont8()`

### Calligraphy

- `Blackletter()`
- `Italic()`

### Blinking

- `BlinkFast()`
- `BlinkSlow()`

### Framing

- `Circle()`
- `Box()`

### Concealing

- `Conceal()`

### Ideograms

- `DoubleLineOverOrLeft()`
- `DoubleLineUnderOrRight()`
- `SingleLineOverOrLeft()`
- `SingleLineUnderOrRight()`
- `Stress()`

### Underline

- `SingleUnderline()`
- `DoubleUnderline()`

### Weight

- `Heavy()` (aka **bold**)
- `Light()`

### Invert

- `Invert()`

### Overline

- `Overline()`

### Proportional spacing

- `ProportionalSpacing()`

### Strikethrough

- `Strike()`


## Examples

To make a string bold:

```python
from ansiscape.strings import Heavy

text = Heavy("This is bold.")
print(text)
```

To make a subset of a string bold:

```python
from ansiscape.strings import Heavy, Sequence

text = Sequence("This is ", Heavy("bold"), ".")
print(text)
```

Note that `Sequence` only holds formatted and unformatted strings and doesn't change the result.

To colour a subset of a string red, with a nested subset coloured yellow:

```python
from ansiscape.strings import Red, Sequence, Yellow

text = Sequence(
    "Kirk said space is ",
    Red(
        "the ",
        Yellow("final"),
        " frontier",
    ),
    '.',
)
print(text)
```
