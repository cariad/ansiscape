from enum import IntEnum, unique


@unique
class StandardColor(IntEnum):
    DEFAULT = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    BLUE = 5
    MAGENTA = 6
    CYAN = 7
    WHITE = 8
