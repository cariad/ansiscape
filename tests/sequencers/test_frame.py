from typing import Optional

from pytest import mark

from ansiscape.enums import Frame, InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers import FrameSequencer
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert FrameSequencer().key == InterpretationKey.FRAME


@mark.parametrize(
    "frame, expect",
    [
        (None, SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF)),
        (Frame.ENCIRCLED, SequencerResult(sgr=SelectGraphicRendition.FRAME_CIRCLE)),
        (Frame.FRAMED, SequencerResult(sgr=SelectGraphicRendition.FRAME_FRAME)),
        (Frame.NONE, SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF)),
    ],
)
def test_resolve(frame: Optional[Frame], expect: SequencerResult) -> None:
    assert FrameSequencer().resolve(frame) == expect
