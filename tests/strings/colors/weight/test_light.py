from ansiscape.enums import Weight
from ansiscape.strings import Light


def test_weight() -> None:
    assert Light().weight == Weight.LIGHT


def test_string() -> None:
    assert str(Light("light")) == "\033[2mlight\033[22m"
