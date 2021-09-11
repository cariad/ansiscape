from ansiscape.enums import StandardColor
from ansiscape.strings import White


def test_color() -> None:
    assert White().color == StandardColor.WHITE


def test_string() -> None:
    assert str(White("white")) == "\033[38;5;7mwhite\033[39m"
