from ansiscape.strings import Overline


def test_string() -> None:
    assert str(Overline("overline")) == "\033[53moverline\033[55m"
