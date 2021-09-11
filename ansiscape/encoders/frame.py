from typing import Dict, Optional

from ansiscape.encoders.enum import EnumSequencer
from ansiscape.enums import Frame, InterpretationKey, SelectGraphicRendition
from ansiscape.types import SequencerResult


class FrameSequencer(EnumSequencer[Frame]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.FRAME

    @property
    def lookup(self) -> Dict[Optional[Frame], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF),
            Frame.CIRCLE: SequencerResult(sgr=SelectGraphicRendition.FRAME_CIRCLE),
            Frame.BOX: SequencerResult(sgr=SelectGraphicRendition.FRAME_BOX),
            Frame.NONE: SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF),
        }
