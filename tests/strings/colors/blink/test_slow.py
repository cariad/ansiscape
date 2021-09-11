from ansiscape.enums import Blink
from ansiscape.strings import BlinkSlow


def test_blink() -> None:
    assert BlinkSlow().blink == Blink.SLOW


def test_string() -> None:
    assert str(BlinkSlow("blink slow")) == "\033[5mblink slow\033[25m"
