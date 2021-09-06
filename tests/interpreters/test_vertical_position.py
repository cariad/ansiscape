from typing import List, Optional

from pytest import mark

from ansiscape.enums import VerticalPosition
from ansiscape.interpreters import InterpretationDict, VerticalPositionInterpreter


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, VerticalPosition.NONE),
        ([72], 0, None),
        ([73], 1, VerticalPosition.SUPERSCRIPT),
        ([74], 1, VerticalPosition.SUBSCRIPT),
        ([75], 1, VerticalPosition.NONE),
        ([76], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[VerticalPosition],
    interpretation: InterpretationDict,
) -> None:
    assert VerticalPositionInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
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
        vertical_position=expect,
    )
