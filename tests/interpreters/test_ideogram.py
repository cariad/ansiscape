from typing import List, Optional

from pytest import mark

from ansiscape.enums import Ideogram
from ansiscape.interpreters import IdeogramInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, Ideogram.NONE),
        ([59], 0, None),
        ([60], 1, Ideogram.LINE_UNDER_OR_RIGHT),
        ([61], 1, Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT),
        ([62], 1, Ideogram.LINE_OVER_OR_LEFT),
        ([63], 1, Ideogram.DOUBLE_LINE_OVER_OR_LEFT),
        ([64], 1, Ideogram.STRESS),
        ([65], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Ideogram],
    interpretation: InterpretationDict,
) -> None:
    assert IdeogramInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=None,
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=None,
        frame=None,
        ideogram=expect,
        intensity=None,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
