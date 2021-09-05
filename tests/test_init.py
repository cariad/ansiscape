from pytest import mark

from ansiscape import InterpretationDict, interpret
from ansiscape.enums import Intensity, VerticalPosition


@mark.parametrize(
    "code, expect",
    [
        (
            "",
            InterpretationDict(
                intensity=None,
                vertical_position=None,
            ),
        ),
        (
            "-1",
            InterpretationDict(
                intensity=None,
                vertical_position=None,
            ),
        ),
        (
            "-1;73",
            InterpretationDict(
                intensity=None,
                vertical_position=None,
            ),
        ),
        (
            "0",
            InterpretationDict(
                intensity=Intensity.NORMAL,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
        (
            "1",
            InterpretationDict(
                intensity=Intensity.BOLD,
                vertical_position=None,
            ),
        ),
        (
            "2",
            InterpretationDict(
                intensity=Intensity.DIM,
                vertical_position=None,
            ),
        ),
        (
            "73",
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "74",
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.SUBSCRIPT,
            ),
        ),
        (
            "75",
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.NONE,
            ),
        ),
        (
            "73;1",
            InterpretationDict(
                intensity=Intensity.BOLD,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "0;73",
            InterpretationDict(
                intensity=Intensity.NORMAL,
                vertical_position=VerticalPosition.SUPERSCRIPT,
            ),
        ),
        (
            "73;74",
            InterpretationDict(
                intensity=None,
                vertical_position=VerticalPosition.SUBSCRIPT,
            ),
        ),
    ],
)
def test_interpret(code: str, expect: InterpretationDict) -> None:
    assert interpret(code) == expect
