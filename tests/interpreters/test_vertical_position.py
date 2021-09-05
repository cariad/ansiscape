from typing import List

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
        (
            [0],
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
        (
            [73],
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            [74],
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.SUBSCRIPT,
            ),
        ),
        (
            [75],
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
    ],
)
def test_update(
    code: List[int],
    expect: InterpretationDict,
    interpretation: InterpretationDict,
) -> None:
    VerticalPositionInterpreter().update(code, interpretation)
    assert interpretation == expect
