from typing import Optional

from ansiscape.encoders.sequencer import Sequencer
from ansiscape.enums import Calligraphy, InterpretationKey, SelectGraphicRendition
from ansiscape.types import SequencerResult


class CalligraphySequencer(Sequencer[Calligraphy]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.CALLIGRAPHY

    def resolve(self, value: Optional[Calligraphy]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        if value == Calligraphy.BLACKLETTER:
            return SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER)

        if value == Calligraphy.ITALIC:
            return SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_ITALIC)

        return SequencerResult(sgr=SelectGraphicRendition.CALLIGRAPHY_NONE)
