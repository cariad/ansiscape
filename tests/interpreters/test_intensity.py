from typing import List, Optional

from pytest import mark

from ansiscape.enums import Intensity
from ansiscape.interpreters import IntensityInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([1], 1),
        ([2], 1),
        ([3], 0),
        ([21], 0),
        ([22], 1),
        ([23], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert IntensityInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], Intensity.NORMAL),
        ([1], Intensity.BOLD),
        ([2], Intensity.DIM),
        ([22], Intensity.NORMAL),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[Intensity],
    interpretation: InterpretationDict,
) -> None:
    IntensityInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        frame=None,
        ideogram=None,
        intensity=expect,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
