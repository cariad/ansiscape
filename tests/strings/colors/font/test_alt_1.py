from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont1


def test_font() -> None:
    assert AlternativeFont1().font == Font.ALT_1


def test_string() -> None:
    assert str(AlternativeFont1("font")) == "\033[12mfont\033[10m"
