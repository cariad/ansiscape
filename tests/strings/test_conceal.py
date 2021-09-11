from ansiscape.strings import Conceal


def test_string() -> None:
    assert str(Conceal("conceal")) == "\033[8mconceal\033[28m"
