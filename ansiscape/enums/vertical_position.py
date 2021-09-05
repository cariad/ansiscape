from enum import IntEnum, unique


@unique
class VerticalPosition(IntEnum):
    NONE = 0
    SUBSCRIPT = 1
    SUPERSCRIPT = 2
