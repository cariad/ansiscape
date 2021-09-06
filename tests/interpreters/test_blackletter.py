from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import BlackletterInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, False),
        ([19], 0, None),
        ([20], 1, True),
        ([21], 0, None),
        ([22], 0, None),
        ([23], 1, False),
        ([24], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    assert BlackletterInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=None,
        blackletter=expect,
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
        underline_color=None,
        vertical_position=None,
    )
