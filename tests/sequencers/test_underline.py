from typing import Optional

from pytest import mark

from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Underline
from ansiscape.sequencers import UnderlineSequencer
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert UnderlineSequencer().key == InterpretationKey.UNDERLINE


@mark.parametrize(
    "underline, expect",
    [
        (None, SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_NONE)),
        (
            Underline.DOUBLE,
            SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_DOUBLE),
        ),
        (
            Underline.SINGLE,
            SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_SINGLE),
        ),
        (Underline.NONE, SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_NONE)),
    ],
)
def test_resolve(underline: Optional[Underline], expect: SequencerResult) -> None:
    assert UnderlineSequencer().resolve(underline) == expect
