from io import StringIO
from typing import List, Tuple

from pytest import mark

from ansiscape import Sequence, red, yellow
from ansiscape.enums import Blink, Calligraphy, MetaInterpretation, NamedColor, Weight
from ansiscape.types import Interpretation, SequencePart


def test_extend() -> None:
    r = red("foo")
    y = yellow("bar")
    r.extend(y)
    assert r.parts == [
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=MetaInterpretation.REVERT),
        y,
    ]


def test_encoded() -> None:
    sequence = Sequence(
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=MetaInterpretation.REVERT),
    )
    assert sequence.encoded == "\033[31mfoo\033[39m"


@mark.parametrize(
    "stack, expect",
    [
        (
            [
                Interpretation(background=NamedColor.BLUE),
                Interpretation(background=NamedColor.RED),
                Interpretation(background=MetaInterpretation.REVERT),
            ],
            "\033[44m",
        ),
        (
            [
                Interpretation(background=NamedColor.BLUE),
                Interpretation(calligraphy=Calligraphy.ITALIC),
                Interpretation(background=NamedColor.RED),
                Interpretation(background=MetaInterpretation.REVERT),
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
                Interpretation(foreground=(1.0, 0.0, 0.0, 1)),
            ],
            "\033[38;2;255;0;0m",
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
        Interpretation(foreground=MetaInterpretation.REVERT),
        Interpretation(foreground=NamedColor.YELLOW),
        "bar",
        Interpretation(foreground=MetaInterpretation.REVERT),
    ]


@mark.parametrize(
    "parts, expect",
    [
        ((), []),
        (("",), []),
        (("foo",), ["foo"]),
        (("\033[44m",), [Interpretation(background=NamedColor.BLUE)]),
        (("\\033[44m",), ["\\033[44m"]),
        (("\033[8;44m",), [Interpretation(background=NamedColor.BLUE, conceal=True)]),
        (
            ("\033[8m\033[44m",),
            [Interpretation(background=NamedColor.BLUE, conceal=True)],
        ),
        (
            ("\033[8mfoo\033[44m",),
            [
                Interpretation(conceal=True),
                "foo",
                Interpretation(background=NamedColor.BLUE),
            ],
        ),
        (
            ("bar\033[8mfoo\033[44m",),
            [
                "bar",
                Interpretation(conceal=True),
                "foo",
                Interpretation(background=NamedColor.BLUE),
            ],
        ),
        (
            ("\033[8mfoo\033[44mbar",),
            [
                Interpretation(conceal=True),
                "foo",
                Interpretation(background=NamedColor.BLUE),
                "bar",
            ],
        ),
    ],
)
def test_init__with_codes(
    parts: Tuple[SequencePart, ...],
    expect: List[SequencePart],
) -> None:
    assert Sequence(*parts).parts == expect


def test_resolved() -> None:
    child_string_string = Sequence(
        "hello",
        "world",
    )

    child_string_interpretation = Sequence(
        "goodbye",
        Interpretation(calligraphy=Calligraphy.ITALIC),
        "bobby",
        Interpretation(calligraphy=MetaInterpretation.REVERT),
    )

    child_interpretation_string = Sequence(
        Interpretation(calligraphy=Calligraphy.BLACKLETTER),
        "welcome",
        Interpretation(calligraphy=MetaInterpretation.REVERT),
        "jimmy",
    )

    child_interpretation_interpretation = Sequence(
        Interpretation(blink=Blink.SLOW),
        "wow",
        Interpretation(blink=MetaInterpretation.REVERT),
    )

    sequence = Sequence(
        Interpretation(foreground=NamedColor.YELLOW),
        "woo",
        Interpretation(foreground=MetaInterpretation.REVERT),
        "boo",
        Interpretation(weight=Weight.HEAVY),
        Interpretation(foreground=NamedColor.RED),
        "foo",
        "bar",
        child_string_string,
        "done",
        child_string_interpretation,
        Interpretation(foreground=MetaInterpretation.REVERT),
        Interpretation(weight=MetaInterpretation.REVERT),
        child_interpretation_interpretation,
        Interpretation(background=NamedColor.CYAN),
        child_interpretation_string,
        "jar",
        "goo",
        "moo",
        Interpretation(background=MetaInterpretation.REVERT),
    )

    assert list(sequence.resolved) == [
        Interpretation(foreground=NamedColor.YELLOW),
        "woo",
        Interpretation(foreground=MetaInterpretation.REVERT),
        "boo",
        Interpretation(foreground=NamedColor.RED, weight=Weight.HEAVY),
        "foobarhelloworlddonegoodbye",
        Interpretation(calligraphy=Calligraphy.ITALIC),
        "bobby",
        Interpretation(
            blink=Blink.SLOW,
            calligraphy=MetaInterpretation.REVERT,
            foreground=MetaInterpretation.REVERT,
            weight=MetaInterpretation.REVERT,
        ),
        "wow",
        Interpretation(
            blink=MetaInterpretation.REVERT,
            calligraphy=Calligraphy.BLACKLETTER,
            background=NamedColor.CYAN,
        ),
        "welcome",
        Interpretation(calligraphy=MetaInterpretation.REVERT),
        "jimmyjargoomoo",
        Interpretation(background=MetaInterpretation.REVERT),
    ]


def test_str() -> None:
    sequence = Sequence(
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=MetaInterpretation.REVERT),
    )
    assert str(sequence) == "\033[31mfoo\033[39m"


def test_write_json() -> None:
    sequence = Sequence(
        Interpretation(foreground=NamedColor.RED),
        "foo",
        Interpretation(foreground=MetaInterpretation.REVERT),
    )
    json_io = StringIO()
    sequence.write_json(json_io)
    assert json_io.getvalue() == '[{"foreground": 1},"foo",{"foreground": -2}]\n'
