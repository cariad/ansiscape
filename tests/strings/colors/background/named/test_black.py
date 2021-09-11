from ansiscape.enums import StandardColor
from ansiscape.strings import BlackBackground


def test_color() -> None:
    assert BlackBackground().color == StandardColor.BLACK


def test_string() -> None:
    assert str(BlackBackground("black")) == "\033[48;5;0mblack\033[49m"
