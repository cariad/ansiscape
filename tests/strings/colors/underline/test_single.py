from ansiscape.enums import Underline
from ansiscape.strings import SingleUnderline


def test_underline() -> None:
    assert SingleUnderline().underline == Underline.SINGLE


def test_string() -> None:
    assert str(SingleUnderline("underline")) == "\033[4munderline\033[24m"
