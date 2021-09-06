from typing import List, Optional

from pytest import mark

from ansiscape.enums import Underline
from ansiscape.interpreters import UnderlineInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, Underline.NONE),
        ([3], 0, None),
        ([4], 1, Underline.SINGLE),
        ([5], 0, None),
        ([20], 0, None),
        ([21], 1, Underline.DOUBLE),
        ([22], 0, None),
        ([23], 0, None),
        ([24], 1, Underline.NONE),
        ([25], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Underline],
    interpretation: InterpretationDict,
) -> None:
    assert UnderlineInterpreter().update(code, interpretation) == expect_claim
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
        underline=expect,
        vertical_position=None,
    )
