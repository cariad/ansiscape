from typing import List

from pytest import mark

from ansiscape import Sequence, red, yellow
from ansiscape.enums import (
    Blink,
    Calligraphy,
    InterpretationSpecial,
    NamedColor,
    Weight,
)
from ansiscape.types import Interpretation


def test_extend() -> None:
    r = red("foo")
    y = yellow("bar")
    r.extend(y)
    assert r.parts == (
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
        y,
    )


def test_encoded() -> None:
    sequence = Sequence(
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
    )
    assert sequence.encoded == "\033[31mfoo\033[39m"


@mark.parametrize(
    "stack, expect",
    [
        (
            [
                Interpretation(background=NamedColor.BLUE),
                Interpretation(background=NamedColor.RED),
                Interpretation(background=InterpretationSpecial.REVERT),
            ],
            "\033[44m",
        ),
        (
            [
                Interpretation(background=NamedColor.BLUE),
                Interpretation(calligraphy=Calligraphy.ITALIC),
                Interpretation(background=NamedColor.RED),
                Interpretation(background=InterpretationSpecial.REVERT),
            ],
            "\033[44m",
        ),
        (
            [
                Interpretation(overline=True, weight=Weight.LIGHT),
            ],
            "\033[53;2m",
        ),
        (
            [
                Interpretation(foreground=(1.0, 0.0, 0.0, 1), weight=Weight.LIGHT),
            ],
            "\033[2m\033[38;2;255;0;0m",
        ),
    ],
)
def test_encode_escape_sequence(stack: List[Interpretation], expect: str) -> None:
    assert Sequence.encode_escape_sequence(stack=stack, index=len(stack) - 1) == expect


def test_flatten() -> None:
    r = red("foo")
    y = yellow("bar")
    r.extend(y)
    assert list(r.flatten) == [
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
        Interpretation(foreground=NamedColor.YELLOW),
        "bar",
        Interpretation(foreground=InterpretationSpecial.REVERT),
    ]


def test_resolved() -> None:
    child_string_string = Sequence(
        "hello",
        "world",
    )

    child_string_interpretation = Sequence(
        "goodbye",
        Interpretation(calligraphy=Calligraphy.ITALIC),
        "bobby",
        Interpretation(calligraphy=InterpretationSpecial.REVERT),
    )

    child_interpretation_string = Sequence(
        Interpretation(calligraphy=Calligraphy.BLACKLETTER),
        "welcome",
        Interpretation(calligraphy=InterpretationSpecial.REVERT),
        "jimmy",
    )

    child_interpretation_interpretation = Sequence(
        Interpretation(blink=Blink.SLOW),
        "wow",
        Interpretation(blink=InterpretationSpecial.REVERT),
    )

    sequence = Sequence(
        Interpretation(foreground=NamedColor.YELLOW),
        "woo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
        "boo",
        Interpretation(weight=Weight.HEAVY),
        Interpretation(foreground=NamedColor.RED),
        "foo",
        "bar",
        child_string_string,
        "done",
        child_string_interpretation,
        Interpretation(foreground=InterpretationSpecial.REVERT),
        Interpretation(weight=InterpretationSpecial.REVERT),
        child_interpretation_interpretation,
        Interpretation(background=NamedColor.CYAN),
        child_interpretation_string,
        "jar",
        "goo",
        "moo",
        Interpretation(background=InterpretationSpecial.REVERT),
    )

    assert list(sequence.resolved) == [
        Interpretation(foreground=NamedColor.YELLOW),
        "woo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
        "boo",
        Interpretation(foreground=NamedColor.RED, weight=Weight.HEAVY),
        "foobarhelloworlddonegoodbye",
        Interpretation(calligraphy=Calligraphy.ITALIC),
        "bobby",
        Interpretation(
            blink=Blink.SLOW,
            calligraphy=InterpretationSpecial.REVERT,
            foreground=InterpretationSpecial.REVERT,
            weight=InterpretationSpecial.REVERT,
        ),
        "wow",
        Interpretation(
            blink=InterpretationSpecial.REVERT,
            calligraphy=Calligraphy.BLACKLETTER,
            background=NamedColor.CYAN,
        ),
        "welcome",
        Interpretation(calligraphy=InterpretationSpecial.REVERT),
        "jimmyjargoomoo",
        Interpretation(background=InterpretationSpecial.REVERT),
    ]


def test_str() -> None:
    sequence = Sequence(
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=InterpretationSpecial.REVERT),
    )
    assert str(sequence) == "\033[31mfoo\033[39m"
