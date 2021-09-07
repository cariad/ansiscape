from enum import IntEnum, unique


@unique
class ColorScheme(IntEnum):
    IMPLEMENTATION_DEFINED = 0
    TRANSPARENT = 1
    RGB = 2
    CMY = 3
    CMYB = 4
    EIGHT_BIT = 5
