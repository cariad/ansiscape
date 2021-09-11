from ansiscape.enums import Frame
from ansiscape.strings import Circle


def test_frame() -> None:
    assert Circle().frame == Frame.CIRCLE


def test_string() -> None:
    assert str(Circle("frame")) == "\033[52mframe\033[54m"
