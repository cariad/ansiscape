from pytest import mark

from ansiscape.enums import Calligraphy, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreters.calligraphy import CalligraphyValue
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert CalligraphyValue().key == InterpretationKey.CALLIGRAPHY.value


@mark.parametrize(
    "calligraphy, expect",
    [
        (
            Calligraphy.BLACKLETTER,
            SequencerResult(
                attributes=[SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER.value]
            ),
        ),
        (
            Calligraphy.ITALIC,
            SequencerResult(
                attributes=[SelectGraphicRendition.CALLIGRAPHY_ITALIC.value]
            ),
        ),
        (
            Calligraphy.NONE,
            SequencerResult(attributes=[SelectGraphicRendition.CALLIGRAPHY_NONE.value]),
        ),
    ],
)
def test_to_code(calligraphy: Calligraphy, expect: SequencerResult) -> None:
    assert CalligraphyValue().to_code(calligraphy) == expect
