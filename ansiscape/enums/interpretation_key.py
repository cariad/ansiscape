from enum import Enum, unique


@unique
class InterpretationKey(Enum):
    BACKGROUND = "background"
    BLINK = "blink"
    CALLIGRAPHY = "calligraphy"
    CONCEAL = "conceal"
    IDEOGRAM = "ideogram"
    INVERT = "invert"
    FONT = "font"
    FOREGROUND = "foreground"
    FRAME = "frame"
    OVERLINE = "overline"
    PROPORTIONAL_SPACING = "proportional_spacing"
    STRIKE = "strike"
    UNDERLINE = "underline"
    WEIGHT = "weight"
