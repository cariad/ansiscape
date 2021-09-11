from ansiscape.enums import StandardColor
from ansiscape.strings import BlueBackground


def test_color() -> None:
    assert BlueBackground().color == StandardColor.BLUE


def test_string() -> None:
    assert str(BlueBackground("blue")) == "\033[48;5;4mblue\033[49m"
