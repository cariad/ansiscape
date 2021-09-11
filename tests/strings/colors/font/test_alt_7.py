from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont7


def test_font() -> None:
    assert AlternativeFont7().font == Font.ALT_7


def test_string() -> None:
    assert str(AlternativeFont7("font")) == "\033[18mfont\033[10m"
