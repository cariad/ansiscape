from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont8


def test_font() -> None:
    assert AlternativeFont8().font == Font.ALT_8


def test_string() -> None:
    assert str(AlternativeFont8("font")) == "\033[19mfont\033[10m"
