from ansiscape.enums import StandardColor
from ansiscape.strings import Cyan


def test_color() -> None:
    assert Cyan().color == StandardColor.CYAN


def test_string() -> None:
    assert str(Cyan("cyan")) == "\033[38;5;6mcyan\033[39m"
