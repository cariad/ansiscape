from pytest import mark

from ansiscape.color.schemes import get_color_scheme
from ansiscape.enums import ColorScheme


@mark.parametrize(
    "attribute, expect",
    [
        (0, ColorScheme.IMPLEMENTATION_DEFINED),
        (1, ColorScheme.TRANSPARENT),
        (2, ColorScheme.RGB),
        (3, ColorScheme.CMY),
        (4, ColorScheme.CMYB),
        (5, ColorScheme.EIGHT_BIT),
    ],
)
def test_get_color_scheme(attribute: int, expect: ColorScheme) -> None:
    assert get_color_scheme(attribute) == expect
