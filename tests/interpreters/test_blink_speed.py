from typing import List, Optional

from pytest import mark

from ansiscape.enums import BlinkSpeed
from ansiscape.interpreters import BlinkSpeedInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, BlinkSpeed.NONE),
        ([4], 0, None),
        ([5], 1, BlinkSpeed.SLOW),
        ([6], 1, BlinkSpeed.FAST),
        ([7], 0, None),
        ([24], 0, None),
        ([25], 1, BlinkSpeed.NONE),
        ([26], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[BlinkSpeed],
    interpretation: InterpretationDict,
) -> None:
    assert BlinkSpeedInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=expect,
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
        vertical_position=None,
    )
