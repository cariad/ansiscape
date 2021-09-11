from ansiscape.enums import StandardColor
from ansiscape.strings import BrightMagenta


def test_color() -> None:
    assert BrightMagenta().color == StandardColor.BRIGHT_MAGENTA


def test_string() -> None:
    assert str(BrightMagenta("magenta")) == "\033[38;5;13mmagenta\033[39m"
