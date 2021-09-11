from ansiscape.enums import Font
from ansiscape.strings import AlternateFont3


def test_font() -> None:
    assert AlternateFont3().font == Font.ALT_3


def test_string() -> None:
    assert str(AlternateFont3("font")) == "\033[14mfont\033[10m"
