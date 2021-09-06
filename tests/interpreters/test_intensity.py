from typing import List, Optional

from pytest import mark

from ansiscape.enums import Intensity
from ansiscape.interpreters import IntensityInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, Intensity.NORMAL),
        ([1], 1, Intensity.BOLD),
        ([2], 1, Intensity.DIM),
        ([3], 0, None),
        ([21], 0, None),
        ([22], 1, Intensity.NORMAL),
        ([23], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[Intensity],
    interpretation: InterpretationDict,
) -> None:
    assert IntensityInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=None,
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
