from typing import List, Optional

from pytest import mark

from ansiscape.enums import StandardColor
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
        ([38], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ForegroundColorInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], StandardColor.DEFAULT),
        ([30], StandardColor.BLACK),
        ([31], StandardColor.RED),
        ([32], StandardColor.GREEN),
        ([33], StandardColor.YELLOW),
        ([34], StandardColor.BLUE),
        ([35], StandardColor.MAGENTA),
        ([36], StandardColor.CYAN),
        ([37], StandardColor.WHITE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[StandardColor],
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
