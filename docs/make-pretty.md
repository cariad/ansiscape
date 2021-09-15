# Making pretty text

## Basic formatting

Each of these functions returns a `Sequence` that wraps your text in the appropriate codes to begin and end a particular type of formatting.

You can pass in:

- Plain strings
- Strings with embedded escape codes
- [`Interpretation`](interpretation.md) dictionaries
- Other `Sequence` instances

Key                            | Description
------------------------------ | -----------
`alternative_font_0()`         | Use the first alternative font
`alternative_font_1()`         | Use the second alternative font
`alternative_font_2()`         | Use the third alternative font
`alternative_font_3()`         | Use the fourth alternative font
`alternative_font_4()`         | Use the fifth alternative font
`alternative_font_5()`         | Use the sixth alternative font
`alternative_font_6()`         | Use the seventh alternative font
`alternative_font_7()`         | Use the eighth alternative font
`alternative_font_8()`         | Use the ninth alternative font
`black()`                      | Set the foreground colour to black
`black_background()`           | Set the background colour to black
`blackletter()`                | Blackletter script
`blue()`                       | Set the foreground colour to blue
`blue_background()`            | Set the background colour to blue
`bright_black()`               | Set the foreground colour to bright black
`bright_black_background()`    | Set the background colour to bright black
`bright_blue()`                | Set the foreground colour to bright blue
`bright_blue_background()`     | Set the background colour to bright blue
`bright_cyan()`                | Set the foreground colour to bright cyan
`bright_cyan_background()`     | Set the background colour to bright cyan
`bright_green()`               | Set the foreground colour to bright green
`bright_green_background()`    | Set the background colour to bright green
`bright_magenta()`             | Set the foreground colour to bright magenta
`bright_magenta_background()`  | Set the background colour to bright magenta
`bright_red()`                 | Set the foreground colour to bright red
`bright_red_background()`      | Set the background colour to bright red
`bright_white()`               | Set the foreground colour to bright white
`bright_white_background()`    | Set the background colour to bright white
`bright_yellow()`              | Set the foreground colour to bright yellow
`bright_yellow_background()`   | Set the background colour to bright yellow
`circle()`                     | Encircle
`conceal()`                    | Conceal
`cyan()`                       | Set the foreground colour to cyan
`cyan_background()`            | Set the background colour to cyan
`double_line_under_or_right()` | Double line under or right ideogram
`double_line_over_or_left()`   | Double line over or left ideogram
`double_underline()`           | Double underline
`fast_blink()`                 | Blink rapidly
`frame()`                      | Frame
`green()`                      | Set the foreground colour to green
`green_background()`           | Set the background colour to green
`heavy()`                      | Heavy, also known as _bold_ or _intense_
`invert()`                     | Invert background/foreground colours
`italic()`                     | Italic script
`light()`                      | Light, also known as _dim_ or _faint_
`magenta()`                    | Set the foreground colour to magenta
`magenta_background()`         | Set the background colour to magenta
`overline()`                   | Overline
`proportional_spacing()`       | Proportional spacing
`red()`                        | Set the foreground colour to red
`red_background()`             | Set the background colour to red
`single_line_under_or_right()` | Single line under or right ideogram
`single_line_over_or_left()`   | Single line over or left ideogram
`single_underline()`           | Single underline
`slow_blink()`                 | Blink slowly
`strike()`                     | Strikethrough
`stress()`                     | Stress ideogram
`white()`                      | Set the foreground colour to white
`white_background()`           | Set the background colour to white
`yellow()`                     | Set the foreground colour to yellow
`yellow_background()`          | Set the background colour to yellow

## Custom colours

To specify specific RGBA values for the foreground or background, use the `foreground()` or `background()` function.

These accept the same arguments as the functions above, plus a [`Color`](interpretation.md#color).

## Custom formatting

In addition to the functions above, you can pass [`Interpretation`](interpretation.md) dictionaries into `Sequence` to build specific custom formatting.

For example, to make text heavy and italic in one call:

```python
from ansiscape import Interpretation, Sequence
from ansiscape.enums import Calligraphy, MetaInterpretation, Weight

text = Sequence(
    Interpretation(
        calligraphy=Calligraphy.ITALIC,
        weight=Weight.HEAVY,
    ),
    "Whoa.",
    Interpretation(
        calligraphy=MetaInterpretation.REVERT,
        weight=MetaInterpretation.REVERT,
    ),
)
print(text)
```

!!! danger
    You **must** revert all the properties you change by passing
    `MetaInterpretation.REVERT` otherwise the changes will persist in the
    terminal beyond the lifetime of your script.

## Examples

To print a bold string:

```python
from ansiscape import heavy

text = heavy("This is heavy, Doc.")
print(text)
```

To make a bold substring:

```python
from ansiscape import Sequence, heavy

text = Sequence("This is ", heavy("heavy"), ", Doc.")
print(text)
```

You can nest sequences to, for example, nest colours:

```python
from ansiscape import Sequence, green, yellow

text = Sequence(green("This is ", yellow("heavy"), ", Doc,"), " said Marty.")
print(text)
```
