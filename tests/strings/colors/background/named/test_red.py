from ansiscape.enums import StandardColor
from ansiscape.strings import RedBackground


def test_color() -> None:
    assert RedBackground().color == StandardColor.RED


def test_string() -> None:
    assert str(RedBackground("red")) == "\033[48;5;1mred\033[49m"
