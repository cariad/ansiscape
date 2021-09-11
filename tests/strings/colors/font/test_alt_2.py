from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont2


def test_font() -> None:
    assert AlternativeFont2().font == Font.ALT_2


def test_string() -> None:
    assert str(AlternativeFont2("font")) == "\033[13mfont\033[10m"
