from pytest import mark

from ansiscape.enums import Calligraphy, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreters.calligraphy import CalligraphyValue
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert CalligraphyValue().key == InterpretationKey.CALLIGRAPHY


@mark.parametrize(
    "calligraphy, expect",
    [
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
def test_to_code(calligraphy: Calligraphy, expect: SequencerResult) -> None:
    assert CalligraphyValue().to_code(calligraphy) == expect
