from ansiscape.strings import Invert


def test_string() -> None:
    assert str(Invert("invert")) == "\033[7minvert\033[27m"
