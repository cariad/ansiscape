from typing import List, Optional

from pytest import mark

from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters import ForegroundColorInterpreter
from ansiscape.types import Color, InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        # Reset:
        ([0], 1, Color(color_type=ColorType.DEFAULT, rgb=None, standard_color=None)),
        # Standard colours:
        ([29], 0, None),
        (
            [30],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BLACK,
            ),
        ),
        (
            [31],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.RED,
            ),
        ),
        (
            [32],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.GREEN,
            ),
        ),
        (
            [33],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.YELLOW,
            ),
        ),
        (
            [34],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BLUE,
            ),
        ),
        (
            [35],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.MAGENTA,
            ),
        ),
        (
            [36],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.CYAN,
            ),
        ),
        (
            [37],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.WHITE,
            ),
        ),
        # 24-bit:
        (
            [38, 2, 0, 128, 255],
            5,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0.0, 0.5019607843137255, 1.0),
                standard_color=None,
            ),
        ),
        (
            [38, 2, 999, 255, 128, 0],
            6,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(1.0, 0.5019607843137255, 0.0),
                standard_color=None,
            ),
        ),
        (
            [38, 2, 999, 0, 128, 255, 999],
            7,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0.0, 0.5019607843137255, 1.0),
                standard_color=None,
            ),
        ),
        # 8-bit standard colours:
        (
            [38, 5, 0],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BLACK,
            ),
        ),
        (
            [38, 5, 1],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.RED,
            ),
        ),
        (
            [38, 5, 2],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.GREEN,
            ),
        ),
        (
            [38, 5, 3],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.YELLOW,
            ),
        ),
        (
            [38, 5, 4],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BLUE,
            ),
        ),
        (
            [38, 5, 5],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.MAGENTA,
            ),
        ),
        (
            [38, 5, 6],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.CYAN,
            ),
        ),
        (
            [38, 5, 7],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.WHITE,
            ),
        ),
        # 8-bit standard bright colours:
        (
            [38, 5, 8],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_BLACK,
            ),
        ),
        (
            [38, 5, 9],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_RED,
            ),
        ),
        (
            [38, 5, 10],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_GREEN,
            ),
        ),
        (
            [38, 5, 11],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_YELLOW,
            ),
        ),
        (
            [38, 5, 12],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_BLUE,
            ),
        ),
        (
            [38, 5, 13],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_MAGENTA,
            ),
        ),
        (
            [38, 5, 14],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_CYAN,
            ),
        ),
        (
            [38, 5, 15],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_WHITE,
            ),
        ),
        # 8-bit RGB:
        (
            [38, 5, 16],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0, 0, 0),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 21],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 46],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0, 1, 0),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 51],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(0, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 196],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(1, 0, 0),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 201],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(1, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 226],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(1, 1, 0),
                standard_color=None,
            ),
        ),
        (
            [38, 5, 231],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgb=(1, 1, 1),
                standard_color=None,
            ),
        ),
        ([39], 0, None),
        # Standard bright colours:
        ([89], 0, None),
        (
            [90],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_BLACK,
            ),
        ),
        (
            [91],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_RED,
            ),
        ),
        (
            [92],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_GREEN,
            ),
        ),
        (
            [93],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_YELLOW,
            ),
        ),
        (
            [94],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_BLUE,
            ),
        ),
        (
            [95],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_MAGENTA,
            ),
        ),
        (
            [96],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_CYAN,
            ),
        ),
        (
            [97],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgb=None,
                standard_color=StandardColor.BRIGHT_WHITE,
            ),
        ),
        ([98], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Color],
    interpretation: InterpretationDict,
) -> None:
    assert ForegroundColorInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=expect,
        frame=None,
        ideogram=None,
        intensity=None,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
