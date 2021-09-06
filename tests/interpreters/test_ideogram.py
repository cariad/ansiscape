from typing import List, Optional

from pytest import mark

from ansiscape.enums import Ideogram
from ansiscape.interpreters import IdeogramInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([59], 0),
        ([60], 1),
        ([61], 1),
        ([62], 1),
        ([63], 1),
        ([64], 1),
        ([65], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert IdeogramInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], Ideogram.NONE),
        ([60], Ideogram.LINE_UNDER_OR_RIGHT),
        ([61], Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT),
        ([62], Ideogram.LINE_OVER_OR_LEFT),
        ([63], Ideogram.DOUBLE_LINE_OVER_OR_LEFT),
        ([64], Ideogram.STRESS),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[Ideogram],
    interpretation: InterpretationDict,
) -> None:
    IdeogramInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        frame=None,
        ideogram=expect,
        intensity=None,
        invert=None,
        italic=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
