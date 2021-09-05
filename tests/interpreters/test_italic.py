from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import InterpretationDict, ItalicInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([2], 0),
        ([3], 1),
        ([4], 0),
        ([22], 0),
        ([23], 1),
        ([24], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ItalicInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([3], True),
        ([23], False),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    ItalicInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blink_speed=None,
        intensity=None,
        italic=expect,
        underline=None,
        vertical_position=None,
    )
