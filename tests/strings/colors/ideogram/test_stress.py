from ansiscape.enums import Ideogram
from ansiscape.strings import Stress


def test_ideogram() -> None:
    assert Stress().ideogram == Ideogram.STRESS


def test_string() -> None:
    assert str(Stress("ideogram")) == "\033[64mideogram\033[65m"
