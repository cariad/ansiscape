from ansiscape.strings import ProportionalSpacing


def test_string() -> None:
    assert str(ProportionalSpacing("proportional")) == "\033[26mproportional\033[50m"
