from enum import IntEnum, unique


@unique
class BlinkSpeed(IntEnum):
    NONE = 0
    SLOW = 1
    FAST = 2
