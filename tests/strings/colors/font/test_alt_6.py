from ansiscape.enums import Font
from ansiscape.strings import AlternateFont6


def test_font() -> None:
    assert AlternateFont6().font == Font.ALT_6


def test_string() -> None:
    assert str(AlternateFont6("font")) == "\033[17mfont\033[10m"
