from typing import Optional

from pytest import mark

from ansiscape.encoders import BlinkSequencer
from ansiscape.enums import Blink, InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert BlinkSequencer().key == InterpretationKey.BLINK


@mark.parametrize(
    "blink, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.BLINK_NONE),
        ),
        (
            Blink.FAST,
            SequencerResult(sgr=SelectGraphicRendition.BLINK_FAST),
        ),
        (
            Blink.SLOW,
            SequencerResult(sgr=SelectGraphicRendition.BLINK_SLOW),
        ),
        (
            Blink.NONE,
            SequencerResult(sgr=SelectGraphicRendition.BLINK_NONE),
        ),
    ],
)
def test_resolve(blink: Optional[Blink], expect: SequencerResult) -> None:
    assert BlinkSequencer.resolve(blink) == expect
