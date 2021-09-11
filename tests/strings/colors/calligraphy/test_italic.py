from ansiscape.enums import Calligraphy
from ansiscape.strings import Italic


def test_calligraphy() -> None:
    assert Italic().calligraphy == Calligraphy.ITALIC


def test_string() -> None:
    assert str(Italic("italic")) == "\033[3mitalic\033[23m"
