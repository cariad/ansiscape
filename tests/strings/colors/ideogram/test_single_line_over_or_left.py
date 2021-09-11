from ansiscape.enums import Ideogram
from ansiscape.strings import SingleLineOverOrLeft


def test_ideogram() -> None:
    assert SingleLineOverOrLeft().ideogram == Ideogram.SINGLE_LINE_OVER_OR_LEFT


def test_string() -> None:
    assert str(SingleLineOverOrLeft("ideogram")) == "\033[62mideogram\033[65m"
