from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import InterpretationDict, ProportionalSpacingInterpreter


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([25], 0),
        ([26], 1),
        ([27], 0),
        ([49], 0),
        ([50], 1),
        ([51], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert ProportionalSpacingInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([26], True),
        ([50], False),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    ProportionalSpacingInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        frame=None,
        ideogram=None,
        intensity=None,
        invert=None,
        italic=None,
        proportional_spacing=expect,
        strike=None,
        underline=None,
        vertical_position=None,
    )
