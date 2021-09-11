from ansiscape.enums import Font
from ansiscape.strings import AlternateFont0


def test_font() -> None:
    assert AlternateFont0().font == Font.ALT_0


def test_string() -> None:
    assert str(AlternateFont0("font")) == "\033[11mfont\033[10m"
