from typing import Optional

from pytest import mark

from ansiscape.encoders import CalligraphySequencer
from ansiscape.enums import Calligraphy, InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert CalligraphySequencer().key == InterpretationKey.CALLIGRAPHY


@mark.parametrize(
    "calligraphy, expect",
    [
        (
            None,
            SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_NONE),
        ),
        (
            Calligraphy.BLACKLETTER,
            SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER),
        ),
        (
            Calligraphy.ITALIC,
            SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_ITALIC),
        ),
        (
            Calligraphy.NONE,
            SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_NONE),
        ),
    ],
)
def test_resolve(calligraphy: Optional[Calligraphy], expect: SequencerResult) -> None:
    assert CalligraphySequencer().resolve(calligraphy) == expect
