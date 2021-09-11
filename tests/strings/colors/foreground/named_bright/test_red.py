from ansiscape.enums import StandardColor
from ansiscape.strings import BrightRed


def test_color() -> None:
    assert BrightRed().color == StandardColor.BRIGHT_RED


def test_string() -> None:
    assert str(BrightRed("red")) == "\033[38;5;9mred\033[39m"
