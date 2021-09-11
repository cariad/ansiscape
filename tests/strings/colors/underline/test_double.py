from ansiscape.enums import Underline
from ansiscape.strings import DoubleUnderline


def test_underline() -> None:
    assert DoubleUnderline().underline == Underline.DOUBLE


def test_string() -> None:
    assert str(DoubleUnderline("underline")) == "\033[21munderline\033[24m"
