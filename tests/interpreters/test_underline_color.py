from typing import List, Optional

from pytest import mark

from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters import UnderlineColorInterpreter
from ansiscape.types import Color, InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        # Reset:
        ([0], 1, Color(color_type=ColorType.DEFAULT, rgba=None, standard_color=None)),
        # 24-bit:
        (
            [58, 1],
            2,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.0, 0.0, 0.0),
                standard_color=None,
            ),
        ),
        (
            [58, 2, 0, 128, 255],
            5,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.5019607843137255, 1.0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 2, 999, 255, 128, 0],
            6,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1.0, 0.5019607843137255, 0.0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 2, 999, 0, 128, 255, 999],
            7,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.5019607843137255, 1.0, 1),
                standard_color=None,
            ),
        ),
        # 8-bit standard colours:
        (
            [58, 5, 0],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLACK,
            ),
        ),
        (
            [58, 5, 1],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.RED,
            ),
        ),
        (
            [58, 5, 2],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.GREEN,
            ),
        ),
        (
            [58, 5, 3],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.YELLOW,
            ),
        ),
        (
            [58, 5, 4],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLUE,
            ),
        ),
        (
            [58, 5, 5],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.MAGENTA,
            ),
        ),
        (
            [58, 5, 6],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.CYAN,
            ),
        ),
        (
            [58, 5, 7],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.WHITE,
            ),
        ),
        # 8-bit standard bright colours:
        (
            [58, 5, 8],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLACK,
            ),
        ),
        (
            [58, 5, 9],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_RED,
            ),
        ),
        (
            [58, 5, 10],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_GREEN,
            ),
        ),
        (
            [58, 5, 11],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_YELLOW,
            ),
        ),
        (
            [58, 5, 12],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLUE,
            ),
        ),
        (
            [58, 5, 13],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_MAGENTA,
            ),
        ),
        (
            [58, 5, 14],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_CYAN,
            ),
        ),
        (
            [58, 5, 15],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_WHITE,
            ),
        ),
        # 8-bit RGB:
        (
            [58, 5, 16],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 0, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 21],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 0, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 46],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 1, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 51],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 1, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 196],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 0, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 201],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 0, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 226],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 1, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [58, 5, 231],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 1, 1, 1),
                standard_color=None,
            ),
        ),
        # Default:
        ([59], 1, Color(color_type=ColorType.DEFAULT, rgba=None, standard_color=None)),
        ([60], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Color],
    interpretation: InterpretationDict,
) -> None:
    assert UnderlineColorInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=None,
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=None,
        frame=None,
        ideogram=None,
        intensity=None,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        underline_color=expect,
        vertical_position=None,
    )
