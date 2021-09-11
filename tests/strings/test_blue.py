from ansiscape.enums import StandardColor
from ansiscape.strings import Blue


def test_color() -> None:
    assert Blue().color == StandardColor.BLUE


def test_string() -> None:
    assert str(Blue("blue")) == "\033[38;5;4mblue\033[39m"
