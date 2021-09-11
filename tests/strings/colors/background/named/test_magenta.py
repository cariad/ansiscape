from ansiscape.enums import StandardColor
from ansiscape.strings import MagentaBackground


def test_color() -> None:
    assert MagentaBackground().color == StandardColor.MAGENTA


def test_string() -> None:
    assert str(MagentaBackground("magenta")) == "\033[48;5;5mmagenta\033[49m"
