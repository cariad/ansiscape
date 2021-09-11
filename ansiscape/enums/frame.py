from enum import IntEnum, unique


@unique
class Frame(IntEnum):
    NONE = 0
    BOX = 1
    CIRCLE = 2
