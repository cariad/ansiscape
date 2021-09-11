from ansiscape.enums import StandardColor
from ansiscape.strings import BrightGreenBackground


def test_color() -> None:
    assert BrightGreenBackground().color == StandardColor.BRIGHT_GREEN


def test_string() -> None:
    assert str(BrightGreenBackground("green")) == "\033[48;5;10mgreen\033[49m"
