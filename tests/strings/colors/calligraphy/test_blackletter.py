from ansiscape.enums import Calligraphy
from ansiscape.strings import Blackletter


def test_calligraphy() -> None:
    assert Blackletter().calligraphy == Calligraphy.BLACKLETTER


def test_string() -> None:
    assert str(Blackletter("blackletter")) == "\033[20mblackletter\033[23m"
