from enum import IntEnum, unique


@unique
class Weight(IntEnum):
    LIGHT = -1
    NORMAL = 0
    HEAVY = 1
