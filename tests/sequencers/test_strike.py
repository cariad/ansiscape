from typing import Optional

from pytest import mark

from ansiscape.encoders import StrikeSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert StrikeSequencer().key == InterpretationKey.STRIKE


@mark.parametrize(
    "strike, expect",
    [
        (None, SequencerResult(sgr=SelectGraphicRendition.STRIKE_OFF)),
        (True, SequencerResult(sgr=SelectGraphicRendition.STRIKE_ON)),
        (False, SequencerResult(sgr=SelectGraphicRendition.STRIKE_OFF)),
    ],
)
def test_resolve(strike: Optional[bool], expect: SequencerResult) -> None:
    assert StrikeSequencer().resolve(strike) == expect
