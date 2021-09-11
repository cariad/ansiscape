from ansiscape.enums import Font
from ansiscape.strings import AlternateFont7


def test_font() -> None:
    assert AlternateFont7().font == Font.ALT_7


def test_string() -> None:
    assert str(AlternateFont7("font")) == "\033[18mfont\033[10m"
