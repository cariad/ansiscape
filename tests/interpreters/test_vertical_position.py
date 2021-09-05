from typing import List, Optional

from pytest import mark

from ansiscape.enums import VerticalPosition
from ansiscape.interpreters import InterpretationDict, VerticalPositionInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([72], 0),
        ([73], 1),
        ([74], 1),
        ([75], 1),
        ([76], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert VerticalPositionInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], VerticalPosition.NONE),
        ([73], VerticalPosition.SUPERSCRIPT),
        ([74], VerticalPosition.SUBSCRIPT),
        ([75], VerticalPosition.NONE),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[VerticalPosition],
    interpretation: InterpretationDict,
) -> None:
    VerticalPositionInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blink_speed=None,
        intensity=None,
        invert=None,
        italic=None,
        underline=None,
        vertical_position=expect,
    )
