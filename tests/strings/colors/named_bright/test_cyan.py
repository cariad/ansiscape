from ansiscape.enums import StandardColor
from ansiscape.strings import BrightCyan


def test_color() -> None:
    assert BrightCyan().color == StandardColor.BRIGHT_CYAN


def test_string() -> None:
    assert str(BrightCyan("cyan")) == "\033[38;5;14mcyan\033[39m"
