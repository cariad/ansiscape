from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import ProportionalSpacingInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, False),
        ([25], 0, None),
        ([26], 1, True),
        ([27], 0, None),
        ([49], 0, None),
        ([50], 1, False),
        ([51], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    assert ProportionalSpacingInterpreter().update(code, interpretation) == expect_claim
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
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=expect,
        strike=None,
        underline=None,
        vertical_position=None,
    )
