from ansiscape.enums import Ideogram
from ansiscape.strings import SingleLineUnderOrRight


def test_ideogram() -> None:
    assert SingleLineUnderOrRight().ideogram == Ideogram.SINGLE_LINE_UNDER_OR_RIGHT


def test_string() -> None:
    assert str(SingleLineUnderOrRight("ideogram")) == "\033[60mideogram\033[65m"
