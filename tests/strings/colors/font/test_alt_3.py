from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont3


def test_font() -> None:
    assert AlternativeFont3().font == Font.ALT_3


def test_string() -> None:
    assert str(AlternativeFont3("font")) == "\033[14mfont\033[10m"
