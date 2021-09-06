from typing import List, Optional

from pytest import mark

from ansiscape.enums import BlinkSpeed
from ansiscape.interpreters import BlinkSpeedInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([4], 0),
        ([5], 1),
        ([6], 1),
        ([7], 0),
        ([24], 0),
        ([25], 1),
        ([26], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert BlinkSpeedInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], BlinkSpeed.NONE),
        ([5], BlinkSpeed.SLOW),
        ([6], BlinkSpeed.FAST),
        ([25], BlinkSpeed.NONE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[BlinkSpeed],
    interpretation: InterpretationDict,
) -> None:
    BlinkSpeedInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=expect,
        conceal=None,
        font_face=None,
        intensity=None,
        invert=None,
        italic=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
