from ansiscape.enums import Font
from ansiscape.strings import AlternateFont4


def test_font() -> None:
    assert AlternateFont4().font == Font.ALT_4


def test_string() -> None:
    assert str(AlternateFont4("font")) == "\033[15mfont\033[10m"
