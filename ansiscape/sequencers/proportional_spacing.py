from typing import Dict, Optional

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types.sequencer_result import SequencerResult


class ProportionalSpacingSequencer(EnumSequencer[bool]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.PROPORTIONAL_SPACING

    @property
    def lookup(self) -> Dict[Optional[bool], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_OFF),
            True: SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_ON),
            False: SequencerResult(sgr=SelectGraphicRendition.PROPORTIONAL_SPACING_OFF),
        }
