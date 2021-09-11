from ansiscape.strings import Strike


def test_string() -> None:
    assert str(Strike("strike")) == "\033[9mstrike\033[29m"
