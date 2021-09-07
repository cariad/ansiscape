from typing import List, Optional, Tuple

from pytest import mark, raises

from ansiscape.enums import InterpretationKey, StandardColor
from ansiscape.exceptions import AttributeError
from ansiscape.interpreters.color_value import ColorValue
from ansiscape.types import Color


@mark.parametrize(
    "attrs, expect",
    [
        # Transparent:
        ([1], ((0, 0, 0, 0), 1)),
        # 24-bit RGB non-colour:
        ([2], (None, 1)),
        # 24-bit RGB colour:
        ([2, 0, 0, 0], ((0, 0, 0, 1), 4)),
        # 8-bit named colour:
        ([5, 1], (StandardColor.RED, 2)),
        # 8-bit RGB:
        ([5, 232], ((0.04, 0.04, 0.04, 1.0), 2)),
    ],
)
def test_value(attrs: List[int], expect: Tuple[Optional[Color], int]) -> None:
    cv = ColorValue(InterpretationKey.FOREGROUND)
    assert cv.value(attrs) == expect


@mark.parametrize(
    "attrs, expect",
    [
        ([0], "ansiscape has no custom color scheme (attributes=[0])"),
        ([3], "Cyan-Magenta-Yellow not supported (attributes=[3])"),
        ([4], "Cyan-Magenta-Yellow-Black not supported (attributes=[4])"),
    ],
)
def test_value__invalid(attrs: List[int], expect: str) -> None:
    with raises(AttributeError) as ex:
        ColorValue(InterpretationKey.FOREGROUND).value(attrs)
    assert str(ex.value) == expect
