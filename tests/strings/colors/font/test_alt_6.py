from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont6


def test_font() -> None:
    assert AlternativeFont6().font == Font.ALT_6


def test_string() -> None:
    assert str(AlternativeFont6("font")) == "\033[17mfont\033[10m"
