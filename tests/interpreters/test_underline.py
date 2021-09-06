from typing import List, Optional

from pytest import mark

from ansiscape.enums import Underline
from ansiscape.interpreters import InterpretationDict, UnderlineInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([3], 0),
        ([4], 1),
        ([5], 0),
        ([20], 0),
        ([21], 1),
        ([22], 0),
        ([23], 0),
        ([24], 1),
        ([25], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert UnderlineInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], Underline.NONE),
        ([4], Underline.SINGLE),
        ([21], Underline.DOUBLE),
        ([24], Underline.NONE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[Underline],
    interpretation: InterpretationDict,
) -> None:
    UnderlineInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        frame=None,
        intensity=None,
        invert=None,
        italic=None,
        proportional_spacing=None,
        strike=None,
        underline=expect,
        vertical_position=None,
    )
