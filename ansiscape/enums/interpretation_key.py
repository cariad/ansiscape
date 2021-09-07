from enum import Enum, unique


@unique
class InterpretationKey(Enum):
    BACKGROUND = "background"
    BLINK = "blink"
    CONCEAL = "conceal"
    IDEOGRAM = "ideogram"
    INVERT = "invert"
    ITALIC = "italic"
    FONT = "font"
    FOREGROUND = "foreground"
    FRACKTUR = "fraktur"
    FRAME = "frame"
    OVERLINE = "overline"
    PROPORTIONAL_SPACING = "proportional_spacing"
    STRIKE = "strike"
    UNDERLINE = "underline"
    WEIGHT = "weight"
