from ansiscape.enums import StandardColor
from ansiscape.strings import BrightBlue


def test_color() -> None:
    assert BrightBlue().color == StandardColor.BRIGHT_BLUE


def test_string() -> None:
    assert str(BrightBlue("blue")) == "\033[38;5;12mblue\033[39m"
