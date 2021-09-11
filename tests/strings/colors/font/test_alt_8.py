from ansiscape.enums import Font
from ansiscape.strings import AlternateFont8


def test_font() -> None:
    assert AlternateFont8().font == Font.ALT_8


def test_string() -> None:
    assert str(AlternateFont8("font")) == "\033[19mfont\033[10m"
