from typing import Optional

from pytest import mark

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers import ProportionalSpacingSequencer
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert ProportionalSpacingSequencer().key == InterpretationKey.PROPORTIONAL_SPACING


@mark.parametrize(
    "proportional_spacing, expect",
    [
        (None, SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_OFF)),
        (True, SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_ON)),
        (False, SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_OFF)),
    ],
)
def test_resolve(proportional_spacing: Optional[bool], expect: SequencerResult) -> None:
    assert ProportionalSpacingSequencer().resolve(proportional_spacing) == expect
