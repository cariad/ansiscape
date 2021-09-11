from typing import Optional

from pytest import mark

from ansiscape.encoders import ConcealSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert ConcealSequencer().key == InterpretationKey.CONCEAL


@mark.parametrize(
    "conceal, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.CONCEAL_OFF),
        ),
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
def test_resolve(conceal: Optional[bool], expect: SequencerResult) -> None:
    assert ConcealSequencer().resolve(conceal) == expect
