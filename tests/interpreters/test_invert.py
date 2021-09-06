from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import InvertInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, False),
        ([6], 0, None),
        ([7], 1, True),
        ([8], 0, None),
        ([26], 0, None),
        ([27], 1, False),
        ([28], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    assert InvertInterpreter().update(code, interpretation) == expect_claim
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
        invert=expect,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        underline_color=None,
        vertical_position=None,
    )
