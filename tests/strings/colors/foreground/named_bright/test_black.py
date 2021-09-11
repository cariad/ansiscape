from ansiscape.enums import StandardColor
from ansiscape.strings import BrightBlack


def test_color() -> None:
    assert BrightBlack().color == StandardColor.BRIGHT_BLACK


def test_string() -> None:
    assert str(BrightBlack("black")) == "\033[38;5;8mblack\033[39m"
