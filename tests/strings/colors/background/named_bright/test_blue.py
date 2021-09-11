from ansiscape.enums import StandardColor
from ansiscape.strings import BrightBlueBackground


def test_color() -> None:
    assert BrightBlueBackground().color == StandardColor.BRIGHT_BLUE


def test_string() -> None:
    assert str(BrightBlueBackground("blue")) == "\033[48;5;12mblue\033[49m"
