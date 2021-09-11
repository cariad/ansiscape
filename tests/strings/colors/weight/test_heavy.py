from ansiscape.enums import Weight
from ansiscape.strings import Heavy


def test_weight() -> None:
    assert Heavy().weight == Weight.HEAVY


def test_string() -> None:
    assert str(Heavy("heavy")) == "\033[1mheavy\033[22m"
