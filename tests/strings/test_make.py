from pytest import mark

from ansiscape.strings import Red, Sequence, Yellow


@mark.parametrize(
    "sequence, expect",
    [
        (
            Sequence("Here's some ", Red("red"), "!"),
            "Here's some \033[38;5;1mred\033[39m!",
        ),
        (
            Sequence("Here's some ", Red("red and ", Yellow("yellow"), " too"), "!"),
            "Here's some \033[38;5;1mred and \033[38;5;3myellow\033[38;5;1m too\033[39m!",
        ),
    ],
)
def test_sequence(sequence: Sequence, expect: str) -> None:
    assert str(sequence) == expect
