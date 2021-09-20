# Making Sequences

The `ansiscape.Sequence` class is the workhorse of the `ansiscape` package. An instance of `Sequence` describes a set of text and its formatting.

## Initialising

A `Sequence` is initialised with a list containing any or all of:

- Plain text
- Text with escape codes
- [`Interpretation`](interpretation.md) dictionary
- Other `Sequence` instances

For example, to create a sequence describing `"Hello, world!"` in bold, you _could_ write:

```python
from ansiscape import Sequence

sequence = Sequence("\033[1mHello, world!\033[22m")
```

...but a more readable example might be:

```python
from ansiscape import Interpretation, Sequence
from ansiscape.enums import MetaInterpretation, Weight

sequence = Sequence(
    Interpretation(weight=Weight.HEAVY),
    "Hello, world!",
    Interpretation(weight=MetaInterpretation.REVERT),
)
```

## Extending

A `Sequence` can be extended with further strings, [`Interpretation`](interpretation.md) dictionaries and `Sequence` instances via the `extend()` function.

```python
from ansiscape import Interpretation, Sequence
from ansiscape.enums import MetaInterpretation, Weight

sequence = Sequence(
    Interpretation(weight=Weight.HEAVY),
    "Hello, ",
)
sequence.extend("world!")
sequence.extend(Interpretation(weight=MetaInterpretation.REVERT))
```

## Reverting

`Sequence` is aware of its internal stack and property reversions, so formatting can be nested.

For example, to create a sequence of numbers where `2`-`4` are coloured green and `3` is coloured yellow:

```python
from ansiscape import Interpretation, Sequence
from ansiscape.enums import MetaInterpretation, NamedColor

sequence = Sequence(
    "1 ",
    Interpretation(foreground=NamedColor.GREEN),
    "2 ",
    Interpretation(foreground=NamedColor.YELLOW),
    "3 ",
    Interpretation(foreground=MetaInterpretation.REVERT),
    "4 ",
    Interpretation(foreground=MetaInterpretation.REVERT),
    "5",
)
```

## Formatting helpers

`ansiscape` provides a library of functions that return pre-configured `Sequence` instances for given types of formatting.

Like the `Sequence` class, you can pass in any of all of:

- Plain text
- Text with escape codes
- [`Interpretation`](interpretation.md) dictionary
- Other `Sequence` instances

These helper functions all terminate themselves with an appropriate reversion, so they can be nested.

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

## Custom RGB

To specify specific RGBA values for the foreground or background, use the `foreground()` or `background()` function.

These accept the same arguments as the functions above, plus a [`Color`](interpretation.md#color).
