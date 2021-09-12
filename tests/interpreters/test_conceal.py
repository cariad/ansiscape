from pytest import mark

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreters.conceal import ConcealValue
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert ConcealValue().key == InterpretationKey.CONCEAL


@mark.parametrize(
    "conceal, expect",
    [
        (
            True,
            SequencerResult(sgr=SelectGraphicRendition.CONCEAL_ON),
        ),
        (
            False,
            SequencerResult(sgr=SelectGraphicRendition.CONCEAL_OFF),
        ),
    ],
)
def test_to_code(conceal: bool, expect: SequencerResult) -> None:
    assert ConcealValue().to_code(conceal) == expect
