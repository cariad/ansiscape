from pytest import mark

from ansiscape.enums import Blink, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreters.blink import BlinkValue
from ansiscape.types.sequencer_result import SequencerResult


def test_key() -> None:
    assert BlinkValue().key == InterpretationKey.BLINK.value


@mark.parametrize(
    "blink, expect",
    [
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
def test_to_code(blink: Blink, expect: SequencerResult) -> None:
    assert BlinkValue().to_code(blink) == expect
