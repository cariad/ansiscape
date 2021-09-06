from enum import IntEnum, unique


@unique
class Frame(IntEnum):
    NONE = 0
    FRAMED = 1
    ENCIRCLED = 2
