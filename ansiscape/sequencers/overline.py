from typing import Dict, Optional

from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types.sequencer_result import SequencerResult


class OverlineSequencer(EnumSequencer[bool]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.OVERLINE

    @property
    def lookup(self) -> Dict[Optional[bool], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.OVERLINE_OFF),
            True: SequencerResult(sgr=SelectGraphicRendition.OVERLINE_ON),
            False: SequencerResult(sgr=SelectGraphicRendition.OVERLINE_OFF),
        }
