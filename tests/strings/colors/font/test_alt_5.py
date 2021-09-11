from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont5


def test_font() -> None:
    assert AlternativeFont5().font == Font.ALT_5


def test_string() -> None:
    assert str(AlternativeFont5("font")) == "\033[16mfont\033[10m"
