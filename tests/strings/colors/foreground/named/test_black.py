from ansiscape.enums import StandardColor
from ansiscape.strings import Black


def test_color() -> None:
    assert Black().color == StandardColor.BLACK


def test_string() -> None:
    assert str(Black("black")) == "\033[38;5;0mblack\033[39m"
