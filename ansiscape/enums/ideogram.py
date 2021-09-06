from enum import IntEnum, unique


@unique
class Ideogram(IntEnum):
    NONE = 0
    LINE_UNDER_OR_RIGHT = 1
    DOUBLE_LINE_UNDER_OR_RIGHT = 2
    LINE_OVER_OR_LEFT = 3
    DOUBLE_LINE_OVER_OR_LEFT = 4
    STRESS = 5
