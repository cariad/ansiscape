from enum import IntEnum, unique


@unique
class SelectGraphicRendition(IntEnum):
    DEFAULT = 0
    WEIGHT_HEAVY = 1
    WEIGHT_LIGHT = 2
    CALLIGRAPHY_ITALIC = 3
    UNDERLINE_SINGLE = 4
    BLINK_SLOW = 5
    BLINK_FAST = 6
    INVERT_ON = 7
    CONCEAL_ON = 8
    STRIKE_ON = 9
    FONT_DEFAULT = 10
    FONT_ALT_0 = 11
    FONT_ALT_1 = 12
    FONT_ALT_2 = 13
    FONT_ALT_3 = 14
    FONT_ALT_4 = 15
    FONT_ALT_5 = 16
    FONT_ALT_6 = 17
    FONT_ALT_7 = 18
    FONT_ALT_8 = 19
    CALLIGRAPHY_BLACKLETTER = 20
    UNDERLINE_DOUBLE = 21
    WEIGHT_NORMAL = 22
    CALLIGRAPHY_NONE = 23
    UNDERLINE_NONE = 24
    BLINK_NONE = 25
    PROPORTIONAL_SPACING_ON = 26
    INVERT_OFF = 27
    CONCEAL_OFF = 28
    STRIKE_OFF = 29
    FOREGROUND_BLACK = 30
    FOREGROUND_RED = 31
    FOREGROUND_GREEN = 32
    FOREGROUND_YELLOW = 33
    FOREGROUND_BLUE = 34
    FOREGROUND_MAGENTA = 35
    FOREGROUND_CYAN = 36
    FOREGROUND_WHITE = 37
    FOREGROUND_RGB = 38
    FOREGROUND_DEFAULT = 39
    BACKGROUND_BLACK = 40
    BACKGROUND_RED = 41
    BACKGROUND_GREEN = 42
    BACKGROUND_YELLOW = 43
    BACKGROUND_BLUE = 44
    BACKGROUND_MAGENTA = 45
    BACKGROUND_CYAN = 46
    BACKGROUND_WHITE = 47
    BACKGROUND_RGB = 48
    BACKGROUND_DEFAULT = 49
    PROPORTIONAL_SPACING_OFF = 50
    FRAME_BOX = 51
    FRAME_CIRCLE = 52
    OVERLINE_ON = 53
    FRAME_OFF = 54
    OVERLINE_OFF = 55
    RESERVED_56 = 56
    RESERVED_57 = 57
    RESERVED_58 = 58
    RESERVED_59 = 59
    IDEOGRAM_SINGLE_LINE_UNDER_OR_RIGHT = 60
    IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT = 61
    IDEOGRAM_SINGLE_LINE_OVER_OR_LEFT = 62
    IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT = 63
    IDEOGRAM_STRESS = 64
    IDEOGRAM_NONE = 65
