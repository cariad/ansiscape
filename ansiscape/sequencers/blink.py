from typing import Optional

from ansiscape.enums import Blink, InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.sequencer import Sequencer
from ansiscape.types import SequencerResult


class BlinkSequencer(Sequencer[Blink]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.BLINK

    @classmethod
    def resolve(cls, value: Optional[Blink]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        if value == Blink.FAST:
            return SequencerResult(sgr=SelectGraphicRendition.BLINK_FAST)

        if value == Blink.SLOW:
            return SequencerResult(sgr=SelectGraphicRendition.BLINK_SLOW)

        return SequencerResult(sgr=SelectGraphicRendition.BLINK_NONE)
