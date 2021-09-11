from ansiscape.enums import StandardColor
from ansiscape.strings import BrightGreen


def test_color() -> None:
    assert BrightGreen().color == StandardColor.BRIGHT_GREEN


def test_string() -> None:
    assert str(BrightGreen("green")) == "\033[38;5;10mgreen\033[39m"
