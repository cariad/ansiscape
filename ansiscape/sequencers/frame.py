from typing import Dict, Optional

from ansiscape.enums import Frame, InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.enum import EnumSequencer
from ansiscape.types import SequencerResult


class FrameSequencer(EnumSequencer[Frame]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.FRAME

    @property
    def lookup(self) -> Dict[Optional[Frame], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF),
            Frame.ENCIRCLED: SequencerResult(sgr=SelectGraphicRendition.FRAME_CIRCLE),
            Frame.FRAMED: SequencerResult(sgr=SelectGraphicRendition.FRAME_FRAME),
            Frame.NONE: SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF),
        }
