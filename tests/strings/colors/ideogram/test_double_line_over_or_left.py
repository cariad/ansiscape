from ansiscape.enums import Ideogram
from ansiscape.strings import DoubleLineOverOrLeft


def test_ideogram() -> None:
    assert DoubleLineOverOrLeft().ideogram == Ideogram.DOUBLE_LINE_OVER_OR_LEFT


def test_string() -> None:
    assert str(DoubleLineOverOrLeft("ideogram")) == "\033[63mideogram\033[65m"
