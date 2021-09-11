from typing import Dict, Optional

from ansiscape.encoders.enum import EnumSequencer
from ansiscape.enums import Font, InterpretationKey, SelectGraphicRendition
from ansiscape.types import SequencerResult


class FontSequencer(EnumSequencer[Font]):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.FONT

    @property
    def lookup(self) -> Dict[Optional[Font], SequencerResult]:
        return {
            None: SequencerResult(sgr=SelectGraphicRendition.FONT_DEFAULT),
            Font.ALT_0: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_0),
            Font.ALT_1: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_1),
            Font.ALT_2: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_2),
            Font.ALT_3: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_3),
            Font.ALT_4: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_4),
            Font.ALT_5: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_5),
            Font.ALT_6: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_6),
            Font.ALT_7: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_7),
            Font.ALT_8: SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_8),
            Font.DEFAULT: SequencerResult(sgr=SelectGraphicRendition.FONT_DEFAULT),
        }
