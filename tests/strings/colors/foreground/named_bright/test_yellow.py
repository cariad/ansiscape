from ansiscape.enums import StandardColor
from ansiscape.strings import BrightYellow


def test_color() -> None:
    assert BrightYellow().color == StandardColor.BRIGHT_YELLOW


def test_string() -> None:
    assert str(BrightYellow("yellow")) == "\033[38;5;11myellow\033[39m"
