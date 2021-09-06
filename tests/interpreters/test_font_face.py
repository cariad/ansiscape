from typing import List, Optional

from pytest import mark

from ansiscape.enums import FontFace
from ansiscape.interpreters import FontFaceInterpreter, InterpretationDict


@mark.parametrize(
    "code, expect",
    [
        ([0], 1),
        ([9], 0),
        ([10], 1),
        ([11], 1),
        ([12], 1),
        ([13], 1),
        ([14], 1),
        ([15], 1),
        ([16], 1),
        ([17], 1),
        ([18], 1),
        ([19], 1),
        ([20], 0),
    ],
)
def test_claim(code: List[int], expect: int) -> None:
    assert FontFaceInterpreter().claim(code) == expect


@mark.parametrize(
    "code, expect",
    [
        ([0], FontFace.DEFAULT),
        ([10], FontFace.DEFAULT),
        ([11], FontFace.ALTERNATIVE_0),
        ([12], FontFace.ALTERNATIVE_1),
        ([13], FontFace.ALTERNATIVE_2),
        ([14], FontFace.ALTERNATIVE_3),
        ([15], FontFace.ALTERNATIVE_4),
        ([16], FontFace.ALTERNATIVE_5),
        ([17], FontFace.ALTERNATIVE_6),
        ([18], FontFace.ALTERNATIVE_7),
        ([19], FontFace.ALTERNATIVE_8),
    ],
)
def test_update(
    code: List[int],
    expect: Optional[FontFace],
    interpretation: InterpretationDict,
) -> None:
    FontFaceInterpreter().update(code, interpretation)
    assert interpretation == InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=expect,
        foreground_color=None,
        frame=None,
        ideogram=None,
        intensity=None,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )
