from ansiscape.enums import Font
from ansiscape.strings import AlternateFont1


def test_font() -> None:
    assert AlternateFont1().font == Font.ALT_1


def test_string() -> None:
    assert str(AlternateFont1("font")) == "\033[12mfont\033[10m"
