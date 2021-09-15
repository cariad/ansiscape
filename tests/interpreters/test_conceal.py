from pytest import mark

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreters.conceal import ConcealValue
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert ConcealValue().key == InterpretationKey.CONCEAL.value


@mark.parametrize(
    "conceal, expect",
    [
        (
            True,
            SequencerResult(attributes=[SelectGraphicRendition.CONCEAL_ON.value]),
        ),
        (
            False,
            SequencerResult(attributes=[SelectGraphicRendition.CONCEAL_OFF.value]),
        ),
    ],
)
def test_to_code(conceal: bool, expect: SequencerResult) -> None:
    assert ConcealValue().to_code(conceal) == expect
