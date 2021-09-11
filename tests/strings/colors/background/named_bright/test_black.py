from ansiscape.enums import StandardColor
from ansiscape.strings import BrightBlackBackground


def test_color() -> None:
    assert BrightBlackBackground().color == StandardColor.BRIGHT_BLACK


def test_string() -> None:
    assert str(BrightBlackBackground("black")) == "\033[48;5;8mblack\033[49m"
