from ansiscape.enums import StandardColor
from ansiscape.strings import YellowBackground


def test_color() -> None:
    assert YellowBackground().color == StandardColor.YELLOW


def test_string() -> None:
    assert str(YellowBackground("yellow")) == "\033[48;5;3myellow\033[49m"
