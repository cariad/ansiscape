from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import ConcealInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([7], 0),
        ([8], 1),
        ([9], 0),
        ([27], 0),
        ([28], 1),
        ([29], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ConcealInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([8], True),
        ([28], False),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    ConcealInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=expect,
        font_face=None,
        intensity=None,
        invert=None,
        italic=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
