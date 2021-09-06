from typing import List, Optional

from pytest import mark

from ansiscape.enums import Frame
from ansiscape.interpreters import FrameInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([50], 0),
        ([51], 1),
        ([52], 1),
        ([53], 0),
        ([54], 1),
        ([55], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert FrameInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], Frame.NONE),
        ([51], Frame.FRAMED),
        ([52], Frame.ENCIRCLED),
        ([54], Frame.NONE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[Frame],
    interpretation: InterpretationDict,
) -> None:
    FrameInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=None,
        frame=expect,
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
