from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont0


def test_font() -> None:
    assert AlternativeFont0().font == Font.ALT_0


def test_string() -> None:
    assert str(AlternativeFont0("font")) == "\033[11mfont\033[10m"
