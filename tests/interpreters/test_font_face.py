from typing import List, Optional

from pytest import mark

from ansiscape.enums import FontFace
from ansiscape.interpreters import FontFaceInterpreter
from ansiscape.types import InterpretationDict


@mark.parametrize(
    "code, expect_claim, expect",
    [
        ([0], 1, FontFace.DEFAULT),
        ([9], 0, None),
        ([10], 1, FontFace.DEFAULT),
        ([11], 1, FontFace.ALTERNATIVE_0),
        ([12], 1, FontFace.ALTERNATIVE_1),
        ([13], 1, FontFace.ALTERNATIVE_2),
        ([14], 1, FontFace.ALTERNATIVE_3),
        ([15], 1, FontFace.ALTERNATIVE_4),
        ([16], 1, FontFace.ALTERNATIVE_5),
        ([17], 1, FontFace.ALTERNATIVE_6),
        ([18], 1, FontFace.ALTERNATIVE_7),
        ([19], 1, FontFace.ALTERNATIVE_8),
        ([20], 0, None),
    ],
)
def test_update(
    code: List[int],
    expect_claim: int,
    expect: Optional[FontFace],
    interpretation: InterpretationDict,
) -> None:
    assert FontFaceInterpreter().update(code, interpretation) == expect_claim
    assert interpretation == InterpretationDict(
        background_color=None,
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
