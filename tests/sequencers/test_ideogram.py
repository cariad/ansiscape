from typing import Optional

from pytest import mark

from ansiscape.enums import Ideogram, InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers import IdeogramSequencer
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert IdeogramSequencer().key == InterpretationKey.IDEOGRAM


@mark.parametrize(
    "ideogram, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_NONE),
        ),
        (
            Ideogram.DOUBLE_LINE_OVER_OR_LEFT,
            SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT
            ),
        ),
        (
            Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT,
            SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT
            ),
        ),
        (
            Ideogram.LINE_OVER_OR_LEFT,
            SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_LINE_OVER_OR_LEFT),
        ),
        (
            Ideogram.LINE_UNDER_OR_RIGHT,
            SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_LINE_UNDER_OR_RIGHT),
        ),
        (
            Ideogram.STRESS,
            SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_STRESS),
        ),
        (
            Ideogram.NONE,
            SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_NONE),
        ),
    ],
)
def test_resolve(ideogram: Optional[Ideogram], expect: SequencerResult) -> None:
    assert IdeogramSequencer().resolve(ideogram) == expect
