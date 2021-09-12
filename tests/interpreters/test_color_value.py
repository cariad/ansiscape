from typing import Optional, Tuple

from pytest import mark, raises

from ansiscape.enums import StandardColor
from ansiscape.exceptions import AttributeError
from ansiscape.interpreters.foreground import ForegroundValue
from ansiscape.types import Attributes, Color


@mark.parametrize(
    "attrs, expect",
    [
        # Transparent:
        ([38, 1], ((0, 0, 0, 0), 1)),
        # 24-bit RGB colour:
        ([38, 2, 0, 0, 0], ((0, 0, 0, 1), 4)),
        # 8-bit named colour:
        ([38, 5, 1], (StandardColor.RED, 2)),
        # 8-bit RGB:
        ([38, 5, 232], ((0.04, 0.04, 0.04, 1.0), 2)),
    ],
)
def test_value(attrs: Attributes, expect: Tuple[Optional[Color], int]) -> None:
    cv = ForegroundValue()
    assert cv.from_attributes(attrs) == expect


@mark.parametrize(
    "attrs, expect",
    [
        ([38, 0], "ansiscape has no custom color scheme (attributes=[0])"),
        ([38, 3], "Cyan-Magenta-Yellow not supported (attributes=[3])"),
        ([38, 4], "Cyan-Magenta-Yellow-Black not supported (attributes=[4])"),
    ],
)
def test_value__invalid(attrs: Attributes, expect: str) -> None:
    with raises(AttributeError) as ex:
        ForegroundValue().from_attributes(attrs)
    assert str(ex.value) == expect
