from enum import IntEnum, unique


@unique
class Intensity(IntEnum):
    NORMAL = 0
    DIM = 1
    BOLD = 2
