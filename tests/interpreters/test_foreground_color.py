from typing import List, Optional

from pytest import mark

from ansiscape.enums import Color
from ansiscape.interpreters import ForegroundColorInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        # Reset:
        ([0], 1, Color.DEFAULT),
        # Standard colours:
        ([29], 0, None),
        ([30], 1, Color.BLACK),
        ([31], 1, Color.RED),
        ([32], 1, Color.GREEN),
        ([33], 1, Color.YELLOW),
        ([34], 1, Color.BLUE),
        ([35], 1, Color.MAGENTA),
        ([36], 1, Color.CYAN),
        ([37], 1, Color.WHITE),
        # 8-bit standard colours:
        ([38, 5, 0], 3, Color.BLACK),
        ([38, 5, 1], 3, Color.RED),
        ([38, 5, 2], 3, Color.GREEN),
        ([38, 5, 3], 3, Color.YELLOW),
        ([38, 5, 4], 3, Color.BLUE),
        ([38, 5, 5], 3, Color.MAGENTA),
        ([38, 5, 6], 3, Color.CYAN),
        ([38, 5, 7], 3, Color.WHITE),
        # 8-bit standard bright colours:
        ([38, 5, 8], 3, Color.BRIGHT_BLACK),
        ([38, 5, 9], 3, Color.BRIGHT_RED),
        ([38, 5, 10], 3, Color.BRIGHT_GREEN),
        ([38, 5, 11], 3, Color.BRIGHT_YELLOW),
        ([38, 5, 12], 3, Color.BRIGHT_BLUE),
        ([38, 5, 13], 3, Color.BRIGHT_MAGENTA),
        ([38, 5, 14], 3, Color.BRIGHT_CYAN),
        ([38, 5, 15], 3, Color.BRIGHT_WHITE),
        ([39], 0, None),
        # Standard bright colours:
        ([89], 0, None),
        ([90], 1, Color.BRIGHT_BLACK),
        ([91], 1, Color.BRIGHT_RED),
        ([92], 1, Color.BRIGHT_GREEN),
        ([93], 1, Color.BRIGHT_YELLOW),
        ([94], 1, Color.BRIGHT_BLUE),
        ([95], 1, Color.BRIGHT_MAGENTA),
        ([96], 1, Color.BRIGHT_CYAN),
        ([97], 1, Color.BRIGHT_WHITE),
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
