from typing import Union

from ansiscape.enums import InterpretationKey, SelectGraphicRendition, StandardColor
from ansiscape.handlers import get_color_interpreter, get_interpreter_for_sgr
from ansiscape.types import BaseSequence, Color

Part = Union[str, BaseSequence]


def alternative_font_0(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_0, *parts)


def alternative_font_1(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_1, *parts)


def alternative_font_2(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_2, *parts)


def alternative_font_3(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_3, *parts)


def alternative_font_4(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_4, *parts)


def alternative_font_5(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_5, *parts)


def alternative_font_6(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_6, *parts)


def alternative_font_7(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_7, *parts)


def alternative_font_8(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FONT_ALT_8, *parts)


def black(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_BLACK, *parts)


def black_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_BLACK, *parts)


def blackletter(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER, *parts)


def blue(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_BLUE, *parts)


def blue_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_BLUE, *parts)


def bright_black(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_BLACK, *parts)


def bright_black_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_BLACK, *parts)


def bright_blue(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_BLUE, *parts)


def bright_blue_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_BLUE, *parts)


def bright_cyan(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_CYAN, *parts)


def bright_cyan_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_CYAN, *parts)


def bright_green(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_GREEN, *parts)


def bright_green_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_GREEN, *parts)


def bright_magenta(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_MAGENTA, *parts)


def bright_magenta_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_MAGENTA, *parts)


def bright_red(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_RED, *parts)


def bright_red_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_RED, *parts)


def bright_white(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_WHITE, *parts)


def bright_white_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_WHITE, *parts)


def bright_yellow(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.BRIGHT_YELLOW, *parts)


def bright_yellow_background(*parts: Part) -> BaseSequence:
    return make_background(StandardColor.BRIGHT_YELLOW, *parts)


def circle(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FRAME_CIRCLE, *parts)


def conceal(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.CONCEAL_ON, *parts)


def cyan(*parts: Part) -> BaseSequence:
    return make_foreground(StandardColor.CYAN, *parts)


def cyan_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_CYAN, *parts)


def double_line_under_or_right(*parts: Part) -> BaseSequence:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT, *parts
    )


def double_line_over_or_left(*parts: Part) -> BaseSequence:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT, *parts
    )


def double_underline(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.UNDERLINE_DOUBLE, *parts)


def fast_blink(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BLINK_FAST, *parts)


def frame(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FRAME_BOX, *parts)


def green(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_GREEN, *parts)


def green_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_GREEN, *parts)


def heavy(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.WEIGHT_HEAVY, *parts)


def invert(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.INVERT_ON, *parts)


def italic(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.CALLIGRAPHY_ITALIC, *parts)


def light(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.WEIGHT_LIGHT, *parts)


def magenta(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_MAGENTA, *parts)


def magenta_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_MAGENTA, *parts)


def overline(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.OVERLINE_ON, *parts)


def proportional_spacing(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.PROPORTIONAL_SPACING_ON, *parts)


def red(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_RED, *parts)


def red_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_RED, *parts)


def single_line_under_or_right(*parts: Part) -> BaseSequence:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_UNDER_OR_RIGHT, *parts
    )


def single_line_over_or_left(*parts: Part) -> BaseSequence:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_OVER_OR_LEFT, *parts
    )


def single_underline(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.UNDERLINE_SINGLE, *parts)


def slow_blink(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BLINK_SLOW, *parts)


def strike(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.STRIKE_ON, *parts)


def stress(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.IDEOGRAM_STRESS, *parts)


def white(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_WHITE, *parts)


def white_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_WHITE, *parts)


def yellow(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.FOREGROUND_YELLOW, *parts)


def yellow_background(*parts: Part) -> BaseSequence:
    return make_sequence(SelectGraphicRendition.BACKGROUND_YELLOW, *parts)


def make_sequence(sgr: SelectGraphicRendition, *parts: Part) -> BaseSequence:
    return get_interpreter_for_sgr(sgr).make_sequence_from_attributes(
        [sgr.value], *parts
    )


def make_background(color: Color, *parts: Part) -> BaseSequence:
    return get_color_interpreter(InterpretationKey.BACKGROUND).make_sequence(
        color, *parts
    )


def make_foreground(color: Color, *parts: Part) -> BaseSequence:
    return get_color_interpreter(InterpretationKey.FOREGROUND).make_sequence(
        color, *parts
    )
