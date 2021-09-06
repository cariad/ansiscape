from typing import List, Optional

from pytest import mark

from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters import BackgroundColorInterpreter
from ansiscape.types import Color, InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        # Reset:
        ([0], 1, Color(color_type=ColorType.DEFAULT, rgba=None, standard_color=None)),
        # Standard colours:
        ([39], 0, None),
        (
            [40],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLACK,
            ),
        ),
        (
            [41],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.RED,
            ),
        ),
        (
            [42],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.GREEN,
            ),
        ),
        (
            [43],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.YELLOW,
            ),
        ),
        (
            [44],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLUE,
            ),
        ),
        (
            [45],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.MAGENTA,
            ),
        ),
        (
            [46],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.CYAN,
            ),
        ),
        (
            [47],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.WHITE,
            ),
        ),
        # 24-bit:
        (
            [48, 1],
            2,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.0, 0.0, 0.0),
                standard_color=None,
            ),
        ),
        (
            [48, 2, 0, 128, 255],
            5,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.5019607843137255, 1.0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 2, 999, 255, 128, 0],
            6,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1.0, 0.5019607843137255, 0.0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 2, 999, 0, 128, 255, 999],
            7,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.5019607843137255, 1.0, 1),
                standard_color=None,
            ),
        ),
        # 8-bit standard colours:
        (
            [48, 5, 0],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLACK,
            ),
        ),
        (
            [48, 5, 1],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.RED,
            ),
        ),
        (
            [48, 5, 2],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.GREEN,
            ),
        ),
        (
            [48, 5, 3],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.YELLOW,
            ),
        ),
        (
            [48, 5, 4],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BLUE,
            ),
        ),
        (
            [48, 5, 5],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.MAGENTA,
            ),
        ),
        (
            [48, 5, 6],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.CYAN,
            ),
        ),
        (
            [48, 5, 7],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.WHITE,
            ),
        ),
        # 8-bit standard bright colours:
        (
            [48, 5, 8],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLACK,
            ),
        ),
        (
            [48, 5, 9],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_RED,
            ),
        ),
        (
            [48, 5, 10],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_GREEN,
            ),
        ),
        (
            [48, 5, 11],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_YELLOW,
            ),
        ),
        (
            [48, 5, 12],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLUE,
            ),
        ),
        (
            [48, 5, 13],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_MAGENTA,
            ),
        ),
        (
            [48, 5, 14],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_CYAN,
            ),
        ),
        (
            [48, 5, 15],
            3,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_WHITE,
            ),
        ),
        # 8-bit RGB:
        (
            [48, 5, 16],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 0, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 21],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 0, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 46],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 1, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 51],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(0, 1, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 196],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 0, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 201],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 0, 1, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 226],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 1, 0, 1),
                standard_color=None,
            ),
        ),
        (
            [48, 5, 231],
            3,
            Color(
                color_type=ColorType.EXTENDED,
                rgba=(1, 1, 1, 1),
                standard_color=None,
            ),
        ),
        # Default:
        ([49], 1, Color(color_type=ColorType.DEFAULT, rgba=None, standard_color=None)),
        ([50], 0, None),
        # Standard bright colours:
        ([99], 0, None),
        (
            [100],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLACK,
            ),
        ),
        (
            [101],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_RED,
            ),
        ),
        (
            [102],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_GREEN,
            ),
        ),
        (
            [103],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_YELLOW,
            ),
        ),
        (
            [104],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_BLUE,
            ),
        ),
        (
            [105],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_MAGENTA,
            ),
        ),
        (
            [106],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_CYAN,
            ),
        ),
        (
            [107],
            1,
            Color(
                color_type=ColorType.STANDARD,
                rgba=None,
                standard_color=StandardColor.BRIGHT_WHITE,
            ),
        ),
        ([108], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Color],
    interpretation: InterpretationDict,
) -> None:
    assert BackgroundColorInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=expect,
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
        vertical_position=None,
    )
