from typing import Dict, Optional

from ansiscape.encoders.enum import EnumSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.types.sequencer_result import SequencerResult


class InvertSequencer(EnumSequencer[bool]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.INVERT

    @property
    def lookup(self) -> Dict[Optional[bool], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.INVERT_OFF),
            True: SequencerResult(sgr=SelectGraphicRendition.INVERT_ON),
            False: SequencerResult(sgr=SelectGraphicRendition.INVERT_OFF),
        }
