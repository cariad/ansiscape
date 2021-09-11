from ansiscape.enums import StandardColor
from ansiscape.strings import WhiteBackground


def test_color() -> None:
    assert WhiteBackground().color == StandardColor.WHITE


def test_string() -> None:
    assert str(WhiteBackground("white")) == "\033[48;5;7mwhite\033[49m"
