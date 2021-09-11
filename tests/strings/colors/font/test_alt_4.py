from ansiscape.enums import Font
from ansiscape.strings import AlternativeFont4


def test_font() -> None:
    assert AlternativeFont4().font == Font.ALT_4


def test_string() -> None:
    assert str(AlternativeFont4("font")) == "\033[15mfont\033[10m"
