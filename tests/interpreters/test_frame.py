from typing import List, Optional

from pytest import mark

from ansiscape.enums import Frame
from ansiscape.interpreters import FrameInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, Frame.NONE),
        ([50], 0, None),
        ([51], 1, Frame.FRAMED),
        ([52], 1, Frame.ENCIRCLED),
        ([53], 0, None),
        ([54], 1, Frame.NONE),
        ([55], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Frame],
    interpretation: InterpretationDict,
) -> None:
    assert FrameInterpreter().update(code, interpretation) == expect_claim
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
