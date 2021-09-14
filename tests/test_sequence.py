from ansiscape import red, yellow
from ansiscape.enums import InterpretationSpecial, StandardColor
from ansiscape.types import InterpretationDict


def test_add() -> None:
    assert list(red("foo").extend(yellow("bar")).parts) == [
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        InterpretationDict(foreground=StandardColor.YELLOW),
        "bar",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
    ]
