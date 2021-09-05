from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import InterpretationDict, InvertInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([1], 0),
        ([6], 0),
        ([7], 1),
        ([8], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert InvertInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([7], True),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    InvertInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blink_speed=None,
        intensity=None,
        invert=expect,
        italic=None,
        underline=None,
        vertical_position=None,
    )
