from typing import Optional

from pytest import mark

from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Weight
from ansiscape.sequencers import WeightSequencer
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert WeightSequencer().key == InterpretationKey.WEIGHT


@mark.parametrize(
    "weight, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.WEIGHT_NORMAL),
        ),
        (
            Weight.LIGHT,
            SequencerResult(sgr=SelectGraphicRendition.WEIGHT_LIGHT),
        ),
        (
            Weight.NORMAL,
            SequencerResult(sgr=SelectGraphicRendition.WEIGHT_NORMAL),
        ),
        (
            Weight.HEAVY,
            SequencerResult(sgr=SelectGraphicRendition.WEIGHT_HEAVY),
        ),
    ],
)
def test_resolve(weight: Optional[Weight], expect: SequencerResult) -> None:
    assert WeightSequencer().resolve(weight) == expect
