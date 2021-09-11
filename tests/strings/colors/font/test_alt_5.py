from ansiscape.enums import Font
from ansiscape.strings import AlternateFont5


def test_font() -> None:
    assert AlternateFont5().font == Font.ALT_5


def test_string() -> None:
    assert str(AlternateFont5("font")) == "\033[16mfont\033[10m"
