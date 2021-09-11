from ansiscape.enums import Blink
from ansiscape.strings import BlinkFast


def test_blink() -> None:
    assert BlinkFast().blink == Blink.FAST


def test_string() -> None:
    assert str(BlinkFast("blink fast")) == "\033[6mblink fast\033[25m"
