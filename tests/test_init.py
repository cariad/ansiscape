from pytest import mark

from ansiscape import InterpretationDict, interpret
from ansiscape.enums import VerticalPosition


@mark.parametrize(
    "code, expect",
    [
        ("", InterpretationDict(vertical_position=None)),
        ("-1", InterpretationDict(vertical_position=None)),
        ("-1;73", InterpretationDict(vertical_position=None)),
        ("0", InterpretationDict(vertical_position=VerticalPosition.NONE)),
        ("73", InterpretationDict(vertical_position=VerticalPosition.SUPERSCRIPT)),
        ("74", InterpretationDict(vertical_position=VerticalPosition.SUBSCRIPT)),
        ("75", InterpretationDict(vertical_position=VerticalPosition.NONE)),
        ("0;73", InterpretationDict(vertical_position=VerticalPosition.SUPERSCRIPT)),
        ("73;74", InterpretationDict(vertical_position=VerticalPosition.SUBSCRIPT)),
    ],
)
def test_interpret(code: str, expect: InterpretationDict) -> None:
    assert interpret(code) == expect
