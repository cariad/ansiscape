from enum import IntEnum, unique


@unique
class ColorType(IntEnum):
    DEFAULT = 0
    STANDARD = 1
    EXTENDED = 2
