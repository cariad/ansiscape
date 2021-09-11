from ansiscape.enums import StandardColor
from ansiscape.strings import CyanBackground


def test_color() -> None:
    assert CyanBackground().color == StandardColor.CYAN


def test_string() -> None:
    assert str(CyanBackground("cyan")) == "\033[48;5;6mcyan\033[49m"
