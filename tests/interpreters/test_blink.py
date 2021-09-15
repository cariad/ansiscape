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
            SequencerResult(attributes=[SelectGraphicRendition.BLINK_FAST.value]),
        ),
        (
            Blink.SLOW,
            SequencerResult(attributes=[SelectGraphicRendition.BLINK_SLOW.value]),
        ),
        (
            Blink.NONE,
            SequencerResult(attributes=[SelectGraphicRendition.BLINK_NONE.value]),
        ),
    ],
)
def test_to_code(blink: Blink, expect: SequencerResult) -> None:
    assert BlinkValue().to_code(blink) == expect
