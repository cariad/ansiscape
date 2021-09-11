from ansiscape.enums import Ideogram
from ansiscape.strings import DoubleLineUnderOrRight


def test_ideogram() -> None:
    assert DoubleLineUnderOrRight().ideogram == Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT


def test_string() -> None:
    assert str(DoubleLineUnderOrRight("ideogram")) == "\033[61mideogram\033[65m"
