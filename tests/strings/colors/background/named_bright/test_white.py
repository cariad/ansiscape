from ansiscape.enums import StandardColor
from ansiscape.strings import BrightWhiteBackground


def test_color() -> None:
    assert BrightWhiteBackground().color == StandardColor.BRIGHT_WHITE


def test_string() -> None:
    assert str(BrightWhiteBackground("white")) == "\033[48;5;15mwhite\033[49m"
