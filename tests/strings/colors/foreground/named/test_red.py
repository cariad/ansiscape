from ansiscape.enums import StandardColor
from ansiscape.strings import Red


def test_color() -> None:
    assert Red().color == StandardColor.RED


def test_string() -> None:
    assert str(Red("red")) == "\033[38;5;1mred\033[39m"
