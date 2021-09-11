from ansiscape.enums import StandardColor
from ansiscape.strings import GreenBackground


def test_color() -> None:
    assert GreenBackground().color == StandardColor.GREEN


def test_string() -> None:
    assert str(GreenBackground("green")) == "\033[48;5;2mgreen\033[49m"
