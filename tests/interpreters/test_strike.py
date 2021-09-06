from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import InterpretationDict, StrikeInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([8], 0),
        ([9], 1),
        ([10], 0),
        ([28], 0),
        ([29], 1),
        ([30], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert StrikeInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([9], True),
        ([29], False),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    StrikeInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blink_speed=None,
        conceal=None,
        intensity=None,
        invert=None,
        italic=None,
        strike=expect,
        underline=None,
        vertical_position=None,
    )
