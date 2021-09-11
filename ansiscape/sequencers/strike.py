from typing import Dict, Optional

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types.sequencer_result import SequencerResult


class StrikeSequencer(EnumSequencer[bool]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.STRIKE

    @property
    def lookup(self) -> Dict[Optional[bool], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.STRIKE_OFF),
            True: SequencerResult(sgr=SelectGraphicRendition.STRIKE_ON),
            False: SequencerResult(sgr=SelectGraphicRendition.STRIKE_OFF),
        }
