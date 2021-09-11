from typing import Optional

from ansiscape.encoders.sequencer import Sequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Weight
from ansiscape.types import SequencerResult


class WeightSequencer(Sequencer[Weight]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.WEIGHT

    def resolve(self, value: Optional[Weight]) -> SequencerResult:
        if value == Weight.HEAVY:
            return SequencerResult(sgr=SelectGraphicRendition.WEIGHT_HEAVY)
        if value == Weight.LIGHT:
            return SequencerResult(sgr=SelectGraphicRendition.WEIGHT_LIGHT)
        return SequencerResult(sgr=SelectGraphicRendition.WEIGHT_NORMAL)
