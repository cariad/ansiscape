from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import ConcealInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, False),
        ([7], 0, None),
        ([8], 1, True),
        ([9], 0, None),
        ([27], 0, None),
        ([28], 1, False),
        ([29], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    assert ConcealInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=None,
        blackletter=None,
        blink_speed=None,
        conceal=expect,
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
