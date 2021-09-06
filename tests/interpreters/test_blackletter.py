from typing import List, Optional

from pytest import mark

from ansiscape.interpreters import BlackletterInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([19], 0),
        ([20], 1),
        ([21], 0),
        ([22], 0),
        ([23], 1),
        ([24], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert BlackletterInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], False),
        ([20], True),
        ([23], False),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[bool],
    interpretation: InterpretationDict,
) -> None:
    BlackletterInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=expect,
        blink_speed=None,
        conceal=None,
        font_face=None,
        frame=None,
        intensity=None,
        invert=None,
        italic=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
