from typing import Optional

from pytest import mark

from ansiscape.encoders import InvertSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert InvertSequencer().key == InterpretationKey.INVERT


@mark.parametrize(
    "invert, expect",
    [
        (None, SequencerResult(sgr=SelectGraphicRendition.INVERT_OFF)),
        (True, SequencerResult(sgr=SelectGraphicRendition.INVERT_ON)),
        (False, SequencerResult(sgr=SelectGraphicRendition.INVERT_OFF)),
    ],
)
def test_resolve(invert: Optional[bool], expect: SequencerResult) -> None:
    assert InvertSequencer().resolve(invert) == expect
