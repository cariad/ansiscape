from ansiscape.enums import InterpretationKey, NamedColor, SelectGraphicRendition
from ansiscape.handlers import get_color_interpreter, get_interpreter_for_sgr
from ansiscape.interpreters import register_interpreters
from ansiscape.sequence import Sequence
from ansiscape.types import Color, Interpretation, SequencePart, SequenceType
from ansiscape.version import get_version

register_interpreters()


def alternative_font_0(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_0, *parts)


def alternative_font_1(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_1, *parts)


def alternative_font_2(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_2, *parts)


def alternative_font_3(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_3, *parts)


def alternative_font_4(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_4, *parts)


def alternative_font_5(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_5, *parts)


def alternative_font_6(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_6, *parts)


def alternative_font_7(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_7, *parts)


def alternative_font_8(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FONT_ALT_8, *parts)


def background(color: Color, *parts: SequencePart) -> SequenceType:
    i = get_color_interpreter(InterpretationKey.BACKGROUND)
    return i.make_sequence(color, *parts)


def black(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_BLACK, *parts)


def black_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_BLACK, *parts)


def blackletter(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER, *parts)


def blue(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_BLUE, *parts)


def blue_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_BLUE, *parts)


def bright_black(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_BLACK, *parts)


def bright_black_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_BLACK, *parts)


def bright_blue(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_BLUE, *parts)


def bright_blue_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_BLUE, *parts)


def bright_cyan(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_CYAN, *parts)


def bright_cyan_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_CYAN, *parts)


def bright_green(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_GREEN, *parts)


def bright_green_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_GREEN, *parts)


def bright_magenta(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_MAGENTA, *parts)


def bright_magenta_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_MAGENTA, *parts)


def bright_red(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_RED, *parts)


def bright_red_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_RED, *parts)


def bright_white(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_WHITE, *parts)


def bright_white_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_WHITE, *parts)


def bright_yellow(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.BRIGHT_YELLOW, *parts)


def bright_yellow_background(*parts: SequencePart) -> SequenceType:
    return background(NamedColor.BRIGHT_YELLOW, *parts)


def circle(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FRAME_CIRCLE, *parts)


def conceal(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.CONCEAL_ON, *parts)


def cyan(*parts: SequencePart) -> SequenceType:
    return foreground(NamedColor.CYAN, *parts)


def cyan_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_CYAN, *parts)


def double_line_under_or_right(*parts: SequencePart) -> SequenceType:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT,
        *parts,
    )


def double_line_over_or_left(*parts: SequencePart) -> SequenceType:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT,
        *parts,
    )


def double_underline(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.UNDERLINE_DOUBLE, *parts)


def fast_blink(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BLINK_FAST, *parts)


def foreground(color: Color, *parts: SequencePart) -> SequenceType:
    i = get_color_interpreter(InterpretationKey.FOREGROUND)
    return i.make_sequence(color, *parts)


def frame(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FRAME_BOX, *parts)


def green(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_GREEN, *parts)


def green_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_GREEN, *parts)


def heavy(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.WEIGHT_HEAVY, *parts)


def invert(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.INVERT_ON, *parts)


def italic(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.CALLIGRAPHY_ITALIC, *parts)


def light(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.WEIGHT_LIGHT, *parts)


def magenta(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_MAGENTA, *parts)


def magenta_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_MAGENTA, *parts)


def make_sequence(sgr: SelectGraphicRendition, *parts: SequencePart) -> SequenceType:
    i = get_interpreter_for_sgr(sgr)
    return i.make_sequence(sgr, *parts)


def overline(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.OVERLINE_ON, *parts)


def proportional_spacing(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.PROPORTIONAL_SPACING_ON, *parts)


def red(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_RED, *parts)


def red_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_RED, *parts)


def sequence(*parts: SequencePart) -> SequenceType:
    return Sequence(*parts)


def single_line_under_or_right(*parts: SequencePart) -> SequenceType:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_UNDER_OR_RIGHT,
        *parts,
    )


def single_line_over_or_left(*parts: SequencePart) -> SequenceType:
    return make_sequence(
        SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_OVER_OR_LEFT,
        *parts,
    )


def single_underline(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.UNDERLINE_SINGLE, *parts)


def slow_blink(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BLINK_SLOW, *parts)


def strike(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.STRIKE_ON, *parts)


def stress(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.IDEOGRAM_STRESS, *parts)


def white(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_WHITE, *parts)


def white_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_WHITE, *parts)


def yellow(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.FOREGROUND_YELLOW, *parts)


def yellow_background(*parts: SequencePart) -> SequenceType:
    return make_sequence(SelectGraphicRendition.BACKGROUND_YELLOW, *parts)


__all__ = [
    "get_version",
    "Interpretation",
    "Sequence",
]
