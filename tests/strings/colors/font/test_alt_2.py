from ansiscape.enums import Font
from ansiscape.strings import AlternateFont2


def test_font() -> None:
    assert AlternateFont2().font == Font.ALT_2


def test_string() -> None:
    assert str(AlternateFont2("font")) == "\033[13mfont\033[10m"
