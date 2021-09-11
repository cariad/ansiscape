from ansiscape.enums import Frame
from ansiscape.strings import Box


def test_frame() -> None:
    assert Box().frame == Frame.BOX


def test_string() -> None:
    assert str(Box("frame")) == "\033[51mframe\033[54m"
