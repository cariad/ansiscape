from typing import Dict, Optional

from ansiscape.enums import Ideogram, InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types import SequencerResult


class IdeogramSequencer(EnumSequencer[Ideogram]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.IDEOGRAM

    @property
    def lookup(self) -> Dict[Optional[Ideogram], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_NONE),
            Ideogram.DOUBLE_LINE_OVER_OR_LEFT: SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT
            ),
            Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT: SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT
            ),
            Ideogram.LINE_OVER_OR_LEFT: SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_LINE_OVER_OR_LEFT
            ),
            Ideogram.LINE_UNDER_OR_RIGHT: SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_LINE_UNDER_OR_RIGHT
            ),
            Ideogram.STRESS: SequencerResult(
                sgr=SelectGraphicRendition.IDEOGRAM_STRESS
            ),
            Ideogram.NONE: SequencerResult(sgr=SelectGraphicRendition.IDEOGRAM_NONE),
        }
