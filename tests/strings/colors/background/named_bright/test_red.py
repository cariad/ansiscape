from ansiscape.enums import StandardColor
from ansiscape.strings import BrightRedBackground


def test_color() -> None:
    assert BrightRedBackground().color == StandardColor.BRIGHT_RED


def test_string() -> None:
    assert str(BrightRedBackground("red")) == "\033[48;5;9mred\033[49m"
