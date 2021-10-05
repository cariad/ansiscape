# Interpretation dictionary and enums

The `ansiscape.Interpretation` dictionary describes an interpretation of one or more ANSI escape codes.

## Keys

Key                    | Type                                                                         | Description
---------------------- | ---------------------------------------------------------------------------- | ----
`background`           | [`MetaColor`](#metacolor), [`NamedColor`](#namedcolor), [`RGBA`](#rgba) or [`MetaInterpretation`](#metainterpretation)             | Background colour
`blink`                | [`Blink`](#blink) or [`MetaInterpretation`](#metainterpretation)             | Blink rate
`calligraphy`          | [`Calligraphy`](#calligraphy) or [`MetaInterpretation`](#metainterpretation) | Calligraphy
`conceal`              | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Conceal/reveal
`font`                 | [`Font`](#font) or [`MetaInterpretation`](#metainterpretation)               | Font face
`foreground`           | [`MetaColor`](#metacolor), [`NamedColor`](#namedcolor), [`RGBA`](#rgba) or [`MetaInterpretation`](#metainterpretation)             | Foreground colour
`frame`                | [`Frame`](#frame) or [`MetaInterpretation`](#metainterpretation)             | Framing
`ideogram`             | [`Ideogram`](#ideogram) or [`MetaInterpretation`](#metainterpretation)       | Ideogram
`invert`               | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Invert background/foreground
`overline`             | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Overline
`proportional_spacing` | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Proportional spacing
`strike`               | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Strikethrough
`underline`            | [`Underline`](#underline) or [`MetaInterpretation`](#metainterpretation)     | Underline
`weight`               | [`Weight`](#weight) or [`MetaInterpretation`](#metainterpretation)           | Weight

## Types

### Blink

Import the `Blink` enum from `ansiscape.enums`.

Value        | JSON | Description
------------ | ---- | -----------
`Blink.FAST` | 2    | Blink the text rapidly
`Blink.NONE` | 0    | Do not blink the text
`Blink.SLOW` | 1    | Blink the text slowly

### Calligraphy

Import the `Calligraphy` enum from `ansiscape.enums`.

Value                     | JSON | Description
------------------------- | ---- | -----------
`Calligraphy.BLACKLETTER` | 1    | Blackletter script, also known as _fraktur_ or _gothic_
`Calligraphy.ITALIC`      | 2    | Italic script
`Calligraphy.NONE`        | 0    | No calligraphy

### Font

Import the `Font` enum from `ansiscape.enums`.

Value          | JSON | Description
-------------- | ---: | -----------
`Font.ALT_0`   |    1 | First alternative font
`Font.ALT_1`   |    2 | Second alternative font
`Font.ALT_2`   |    3 | Third alternative font
`Font.ALT_3`   |    4 | Fourth alternative font
`Font.ALT_4`   |    5 | Fifth alternative font
`Font.ALT_5`   |    6 | Sixth alternative font
`Font.ALT_6`   |    7 | Seventh alternative font
`Font.ALT_7`   |    8 | Eighth alternative font
`Font.ALT_8`   |    9 | Ninth alternative font
`Font.DEFAULT` |    0 | The terminal's default font

### Frame

Import the `Frame` enum from `ansiscape.enums`.

Value          | JSON | Description
-------------- | ---: | -----------
`Frame.BOX`    |    1 | Frame
`Frame.CIRCLE` |    2 | Encircle
`Frame.NONE`   |    0 | No framing

### Ideogram

Import the `Ideogram` enum from `ansiscape.enums`.

Value                                 | JSON | Description
------------------------------------- | ---: | -----------
`Ideogram.DOUBLE_LINE_OVER_OR_LEFT`   |    4 | Double line over or left
`Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT` |    2 | Double line under or right
`Ideogram.NONE`                       |    0 | No ideogram
`Ideogram.SINGLE_LINE_OVER_OR_LEFT`   |    3 | Single line over or left
`Ideogram.SINGLE_LINE_UNDER_OR_RIGHT` |    1 | Single line under or right
`Ideogram.STRESS`                     |    5 | Stress

### MetaColor

Import the `MetaColor` enum from `ansiscape.enums`.

Value               | JSON | Description
------------------- | ---: | -----------
`MetaColor.DEFAULT` |   -1 | The terminal's default colour

### MetaInterpretation

Import the `MetaInterpretation` enum from `ansiscape.enums`.

Value                       | JSON | Description
--------------------------- | ---: | -----------
`MetaInterpretation.REVERT` |   -2 | Revert the property to its previous value

### NamedColor

Import the `NamedColor` enum from `ansiscape.enums`.

Value                       | JSON | Description
--------------------------- | ---: | -----------
`NamedColor.BLACK`          |    0 | Black
`NamedColor.BLUE`           |    4 | Blue
`NamedColor.BRIGHT_BLACK`   |    8 | Bright black
`NamedColor.BRIGHT_BLUE`    |   12 | Bright blue
`NamedColor.BRIGHT_CYAN`    |   14 | Bright cyan
`NamedColor.BRIGHT_GREEN`   |   10 | Bright green
`NamedColor.BRIGHT_MAGENTA` |   13 | Bright magenta
`NamedColor.BRIGHT_RED`     |    9 | Bright red
`NamedColor.BRIGHT_WHITE`   |   15 | Bright white
`NamedColor.BRIGHT_YELLOW`  |   11 | Bright yellow
`NamedColor.CYAN`           |    6 | Cyan
`NamedColor.GREEN`          |    2 | Green
`NamedColor.MAGENTA`        |    5 | Magenta
`NamedColor.RED`            |    1 | Red
`NamedColor.WHITE`          |    7 | White
`NamedColor.YELLOW`         |    3 | Yellow

### RGBA

`RGBA` is a tuple of `(float, float, float, int)` describing the red (0.0-1.0), green (0.0-1.0), blue (0.0-1.0) and alpha (0 or 1) components of a colour.

### Underline

Import the `Underline` enum from `ansiscape.enums`.

Value              | JSON | Description
------------------ | ---: | -----------
`Underline.DOUBLE` |    2 | Double underline
`Underline.NONE`   |    0 | No underline
`Underline.SINGLE` |    1 | Single underline

### Weight

Import the `Weight` enum from `ansiscape.enums`.

Value          | JSON | Description
-------------- | ---: | -----------
`Blink.HEAVY`  |    1 | Heavy, also known as _bold_ or _intense_
`Blink.LIGHT`  |   -1 | Light, also known as _dim_ or _faint_
`Blink.NORMAL` |    0 | Normal
