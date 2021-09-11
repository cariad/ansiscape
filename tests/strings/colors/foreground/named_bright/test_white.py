from ansiscape.enums import StandardColor
from ansiscape.strings import BrightWhite


def test_color() -> None:
    assert BrightWhite().color == StandardColor.BRIGHT_WHITE


def test_string() -> None:
    assert str(BrightWhite("white")) == "\033[38;5;15mwhite\033[39m"
