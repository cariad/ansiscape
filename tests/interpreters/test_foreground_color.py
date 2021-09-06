from typing import List, Optional

from pytest import mark

from ansiscape.enums import Color
from ansiscape.interpreters import ForegroundColorInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        # Reset:
        ([0], 1),
        # Standard colours:
        ([29], 0),
        ([30], 1),
        ([31], 1),
        ([32], 1),
        ([33], 1),
        ([34], 1),
        ([35], 1),
        ([36], 1),
        ([37], 1),
        # 8-bit standard colours:
        ([38, 5, 0], 3),
        ([38, 5, 1], 3),
        ([38, 5, 2], 3),
        ([38, 5, 3], 3),
        ([38, 5, 4], 3),
        ([38, 5, 5], 3),
        ([38, 5, 6], 3),
        ([38, 5, 7], 3),
        # 8-bit standard bright colours:
        ([38, 5, 8], 3),
        ([38, 5, 9], 3),
        ([38, 5, 10], 3),
        ([38, 5, 11], 3),
        ([38, 5, 12], 3),
        ([38, 5, 13], 3),
        ([38, 5, 14], 3),
        ([38, 5, 15], 3),
        ([39], 0),
        ([89], 0),
        # Standard bright colours:
        ([90], 1),
        ([91], 1),
        ([92], 1),
        ([93], 1),
        ([94], 1),
        ([95], 1),
        ([96], 1),
        ([97], 1),
        ([98], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ForegroundColorInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        # Reset:
        ([0], Color.DEFAULT),
        # Standard colours:
        ([30], Color.BLACK),
        ([31], Color.RED),
        ([32], Color.GREEN),
        ([33], Color.YELLOW),
        ([34], Color.BLUE),
        ([35], Color.MAGENTA),
        ([36], Color.CYAN),
        ([37], Color.WHITE),
        # 8-bit standard colours:
        ([38, 5, 0], Color.BLACK),
        ([38, 5, 1], Color.RED),
        ([38, 5, 2], Color.GREEN),
        ([38, 5, 3], Color.YELLOW),
        ([38, 5, 4], Color.BLUE),
        ([38, 5, 5], Color.MAGENTA),
        ([38, 5, 6], Color.CYAN),
        ([38, 5, 7], Color.WHITE),
        # 8-bit standard bright colours:
        ([38, 5, 8], Color.BRIGHT_BLACK),
        ([38, 5, 9], Color.BRIGHT_RED),
        ([38, 5, 10], Color.BRIGHT_GREEN),
        ([38, 5, 11], Color.BRIGHT_YELLOW),
        ([38, 5, 12], Color.BRIGHT_BLUE),
        ([38, 5, 13], Color.BRIGHT_MAGENTA),
        ([38, 5, 14], Color.BRIGHT_CYAN),
        ([38, 5, 15], Color.BRIGHT_WHITE),
        # Standard bright colours:
        ([90], Color.BRIGHT_BLACK),
        ([91], Color.BRIGHT_RED),
        ([92], Color.BRIGHT_GREEN),
        ([93], Color.BRIGHT_YELLOW),
        ([94], Color.BRIGHT_BLUE),
        ([95], Color.BRIGHT_MAGENTA),
        ([96], Color.BRIGHT_CYAN),
        ([97], Color.BRIGHT_WHITE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[Color],
    interpretation: InterpretationDict,
) -> None:
    ForegroundColorInterpreter().update(code, interpretation)
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
