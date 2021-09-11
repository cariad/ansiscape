from ansiscape.enums import StandardColor
from ansiscape.strings import BrightYellowBackground


def test_color() -> None:
    assert BrightYellowBackground().color == StandardColor.BRIGHT_YELLOW


def test_string() -> None:
    assert str(BrightYellowBackground("yellow")) == "\033[48;5;11myellow\033[49m"
