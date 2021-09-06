from typing import List, Optional

from pytest import mark

from ansiscape.enums import Color
from ansiscape.interpreters import ForegroundColorInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([29], 0),
        ([30], 1),
        ([31], 1),
        ([32], 1),
        ([33], 1),
        ([34], 1),
        ([35], 1),
        ([36], 1),
        ([37], 1),
        ([38, 5, 0], 3),
        ([38, 5, 1], 3),
        ([38, 5, 2], 3),
        ([38, 5, 3], 3),
        ([38, 5, 4], 3),
        ([38, 5, 5], 3),
        ([38, 5, 6], 3),
        ([38, 5, 7], 3),
        ([39], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ForegroundColorInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], Color.DEFAULT),
        ([30], Color.BLACK),
        ([31], Color.RED),
        ([32], Color.GREEN),
        ([33], Color.YELLOW),
        ([34], Color.BLUE),
        ([35], Color.MAGENTA),
        ([36], Color.CYAN),
        ([37], Color.WHITE),
        ([38, 5, 0], Color.BLACK),
        ([38, 5, 1], Color.RED),
        ([38, 5, 2], Color.GREEN),
        ([38, 5, 3], Color.YELLOW),
        ([38, 5, 4], Color.BLUE),
        ([38, 5, 5], Color.MAGENTA),
        ([38, 5, 6], Color.CYAN),
        ([38, 5, 7], Color.WHITE),
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
