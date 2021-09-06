from enum import IntEnum, unique


@unique
class StandardColor(IntEnum):
    BLACK = 1
    RED = 2
    GREEN = 3
    YELLOW = 4
    BLUE = 5
    MAGENTA = 6
    CYAN = 7
    WHITE = 8

    BRIGHT_BLACK = 9
    BRIGHT_RED = 10
    BRIGHT_GREEN = 11
    BRIGHT_YELLOW = 12
    BRIGHT_BLUE = 13
    BRIGHT_MAGENTA = 14
    BRIGHT_CYAN = 15
    BRIGHT_WHITE = 16
