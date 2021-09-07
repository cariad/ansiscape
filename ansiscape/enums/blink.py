from enum import IntEnum, unique


@unique
class Blink(IntEnum):
    NONE = 0
    SLOW = 1
    FAST = 2
