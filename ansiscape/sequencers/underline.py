from typing import Dict, Optional

from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Underline
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types import SequencerResult


class UnderlineSequencer(EnumSequencer[Underline]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.UNDERLINE

    @property
    def lookup(self) -> Dict[Optional[Underline], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_NONE),
            Underline.NONE: SequencerResult(sgr=SelectGraphicRendition.UNDERLINE_NONE),
            Underline.SINGLE: SequencerResult(
                sgr=SelectGraphicRendition.UNDERLINE_SINGLE
            ),
            Underline.DOUBLE: SequencerResult(
                sgr=SelectGraphicRendition.UNDERLINE_DOUBLE
            ),
        }
