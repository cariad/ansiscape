from ansiscape.enums import StandardColor
from ansiscape.strings import BrightMagentaBackground


def test_color() -> None:
    assert BrightMagentaBackground().color == StandardColor.BRIGHT_MAGENTA


def test_string() -> None:
    assert str(BrightMagentaBackground("magenta")) == "\033[48;5;13mmagenta\033[49m"
