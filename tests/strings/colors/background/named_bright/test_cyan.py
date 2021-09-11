from ansiscape.enums import StandardColor
from ansiscape.strings import BrightCyanBackground


def test_color() -> None:
    assert BrightCyanBackground().color == StandardColor.BRIGHT_CYAN


def test_string() -> None:
    assert str(BrightCyanBackground("cyan")) == "\033[48;5;14mcyan\033[49m"
