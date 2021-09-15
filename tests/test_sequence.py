from typing import List

from pytest import mark

from ansiscape import Sequence, red, yellow
from ansiscape.enums import (
    Blink,
    Calligraphy,
    InterpretationSpecial,
    StandardColor,
    Weight,
)
from ansiscape.types import InterpretationDict


def test_extend() -> None:
    r = red("foo")
    y = yellow("bar")
    r.extend(y)
    assert r.parts == (
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        y,
    )


def test_encoded() -> None:
    sequence = Sequence(
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
    )
    assert sequence.encoded == "\033[31mfoo\033[39m"


@mark.parametrize(
    "stack, expect",
    [
        (
            [
                InterpretationDict(background=StandardColor.BLUE),
                InterpretationDict(background=StandardColor.RED),
                InterpretationDict(background=InterpretationSpecial.REVERT),
            ],
            "\033[44m",
        ),
        (
            [
                InterpretationDict(overline=True, weight=Weight.LIGHT),
            ],
            "\033[53;2m",
        ),
        (
            [
                InterpretationDict(foreground=(1.0, 0.0, 0.0, 1), weight=Weight.LIGHT),
            ],
            "\033[2m\033[38;2;255;0;0m",
        ),
    ],
)
def test_encode_escape_sequence(stack: List[InterpretationDict], expect: str) -> None:
    assert Sequence.encode_escape_sequence(stack=stack, index=len(stack) - 1) == expect


def test_flatten() -> None:
    r = red("foo")
    y = yellow("bar")
    r.extend(y)
    assert list(r.flatten) == [
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        InterpretationDict(foreground=StandardColor.YELLOW),
        "bar",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
    ]


def test_resolved() -> None:
    child_string_string = Sequence(
        "hello",
        "world",
    )

    child_string_interpretation = Sequence(
        "goodbye",
        InterpretationDict(calligraphy=Calligraphy.ITALIC),
        "bobby",
        InterpretationDict(calligraphy=InterpretationSpecial.REVERT),
    )

    child_interpretation_string = Sequence(
        InterpretationDict(calligraphy=Calligraphy.BLACKLETTER),
        "welcome",
        InterpretationDict(calligraphy=InterpretationSpecial.REVERT),
        "jimmy",
    )

    child_interpretation_interpretation = Sequence(
        InterpretationDict(blink=Blink.SLOW),
        "wow",
        InterpretationDict(blink=InterpretationSpecial.REVERT),
    )

    sequence = Sequence(
        InterpretationDict(foreground=StandardColor.YELLOW),
        "woo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        "boo",
        InterpretationDict(weight=Weight.HEAVY),
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        "bar",
        child_string_string,
        "done",
        child_string_interpretation,
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        InterpretationDict(weight=InterpretationSpecial.REVERT),
        child_interpretation_interpretation,
        InterpretationDict(background=StandardColor.CYAN),
        child_interpretation_string,
        "jar",
        "goo",
        "moo",
        InterpretationDict(background=InterpretationSpecial.REVERT),
    )

    assert list(sequence.resolved) == [
        InterpretationDict(foreground=StandardColor.YELLOW),
        "woo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
        "boo",
        InterpretationDict(foreground=StandardColor.RED, weight=Weight.HEAVY),
        "foobarhelloworlddonegoodbye",
        InterpretationDict(calligraphy=Calligraphy.ITALIC),
        "bobby",
        InterpretationDict(
            blink=Blink.SLOW,
            calligraphy=InterpretationSpecial.REVERT,
            foreground=InterpretationSpecial.REVERT,
            weight=InterpretationSpecial.REVERT,
        ),
        "wow",
        InterpretationDict(
            blink=InterpretationSpecial.REVERT,
            calligraphy=Calligraphy.BLACKLETTER,
            background=StandardColor.CYAN,
        ),
        "welcome",
        InterpretationDict(calligraphy=InterpretationSpecial.REVERT),
        "jimmyjargoomoo",
        InterpretationDict(background=InterpretationSpecial.REVERT),
    ]


def test_str() -> None:
    sequence = Sequence(
        InterpretationDict(foreground=StandardColor.RED),
        "foo",
        InterpretationDict(foreground=InterpretationSpecial.REVERT),
    )
    assert str(sequence) == "\033[31mfoo\033[39m"
