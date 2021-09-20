# Interpretation dictionary and enums

The `ansiscape.Interpretation` dictionary describes an interpretation of one or more ANSI escape codes.

## Keys

Key                    | Type                                                                         | Description
---------------------- | ---------------------------------------------------------------------------- | ----
`background`           | [`Color`](#color) or [`MetaInterpretation`](#metainterpretation)             | Background colour
`blink`                | [`Blink`](#blink) or [`MetaInterpretation`](#metainterpretation)             | Blink rate
`calligraphy`          | [`Calligraphy`](#calligraphy) or [`MetaInterpretation`](#metainterpretation) | Calligraphy
`conceal`              | `bool` or [`MetaInterpretation`](#metainterpretation)                        | Conceal/reveal
`font`                 | [`Font`](#font) or [`MetaInterpretation`](#metainterpretation)               | Font face
`foreground`           | [`Color`](#color) or [`MetaInterpretation`](#metainterpretation)             | Foreground colour
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

- `Blink.FAST`: blink the text rapidly
- `Blink.NONE`: do not blink the text
- `Blink.SLOW`: blink the text slowly

### Calligraphy

Import the `Calligraphy` enum from `ansiscape.enums`.

- `Calligraphy.BLACKLETTER`: blackletter script, also known as _fraktur_ or _gothic_.
- `Calligraphy.ITALIC`: italic script.
- `Calligraphy.NONE`: no calligraphy.

### Color

`Color` must be one of:

- `ansiscape.enums.MetaColor` enum: `MetaColor.DEFAULT` to return to the terminal's default colour.
- `ansiscape.enums.NamedColor` enum: `NamedColor.BLACK`, `NamedColor.BRIGHT_YELLOW`, etc.
- `ansiscape.types.RGBA` tuple: `(red: 0.0-1.0, green: 0.0-1.0, blue: 0.0-1.0, alpha: 0 or 1)`

### Font

Import the `Font` enum from `ansiscape.enums`.

- `Font.ALT_0`: first alternative font
- `Font.ALT_1`: second alternative font
- `Font.ALT_2`: third alternative font
- `Font.ALT_3`: fourth alternative font
- `Font.ALT_4`: fifth alternative font
- `Font.ALT_5`: sixth alternative font
- `Font.ALT_6`: seventh alternative font
- `Font.ALT_7`: eighth alternative font
- `Font.ALT_8`: ninth alternative font
- `Font.DEFAULT`: the terminal's default font

### Frame

Import the `Frame` enum from `ansiscape.enums`.

- `Frame.BOX`: frame.
- `Frame.CIRCLE`: encircle.
- `Frame.NONE`: no framing.

### Ideogram

Import the `Ideogram` enum from `ansiscape.enums`.

- `Ideogram.DOUBLE_LINE_OVER_OR_LEFT`: double line over or left
- `Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT`: double line under or right
- `Ideogram.NONE`: no ideogram
- `Ideogram.SINGLE_LINE_OVER_OR_LEFT`: single line over or left
- `Ideogram.SINGLE_LINE_UNDER_OR_RIGHT`: single line under or right
- `Ideogram.STRESS`: stress

### MetaInterpretation

Import the `MetaInterpretation` enum from `ansiscape.enums`.

- `MetaInterpretation.REVERT`: revert the given property to its previous value.

### Underline

Import the `Underline` enum from `ansiscape.enums`.

- `Underline.DOUBLE`: double underline
- `Underline.NONE`: no underline
- `Underline.SINGLE`: single underline

### Weight

Import the `Weight` enum from `ansiscape.enums`.

- `Blink.HEAVY`: heavy, also known as _bold_ or _intense_.
- `Blink.LIGHT`: light, also known as _dim_ or _faint_.
- `Blink.NORMAL`: normal
