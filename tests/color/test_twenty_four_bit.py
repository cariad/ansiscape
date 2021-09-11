from typing import Optional

from pytest import mark, raises

from ansiscape.color.twenty_four_bit import interpret_24_bit_rgb
from ansiscape.exceptions import AttributeError
from ansiscape.types import RGB, Attributes


@mark.parametrize(
    "attrs, expect",
    [
        ([], None),
        ([0, 0, 0], (0, 0, 0)),
        ([255, 255, 255], (1, 1, 1)),
    ],
)
def test_interpret_24_bit_rgb(attrs: Attributes, expect: Optional[RGB]) -> None:
    assert interpret_24_bit_rgb(attrs) == expect


@mark.parametrize(
    "attrs, expect",
    [
        ([0], "color spaces are not supported"),
        ([0, 1], "unexpected sequence"),
        ([0, 1, 2, 3, 4], "color spaces are not supported"),
    ],
)
def test_interpret_24_bit_rgb__fail(attrs: Attributes, expect: str) -> None:
    with raises(AttributeError) as ex:
        interpret_24_bit_rgb(attrs)
    assert str(ex.value) == f"{expect} (attributes={attrs})"
