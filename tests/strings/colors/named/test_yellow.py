from ansiscape.enums import StandardColor
from ansiscape.strings import Yellow


def test_color() -> None:
    assert Yellow().color == StandardColor.YELLOW


def test_string() -> None:
    assert str(Yellow("yellow")) == "\033[38;5;3myellow\033[39m"
