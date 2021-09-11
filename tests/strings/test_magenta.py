from ansiscape.enums import StandardColor
from ansiscape.strings import Magenta


def test_color() -> None:
    assert Magenta().color == StandardColor.MAGENTA


def test_string() -> None:
    assert str(Magenta("magenta")) == "\033[38;5;5mmagenta\033[39m"
