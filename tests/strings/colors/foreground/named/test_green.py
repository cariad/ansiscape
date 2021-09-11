from ansiscape.enums import StandardColor
from ansiscape.strings import Green


def test_color() -> None:
    assert Green().color == StandardColor.GREEN


def test_string() -> None:
    assert str(Green("green")) == "\033[38;5;2mgreen\033[39m"
