from typing import Any, Dict

from ansiscape.encoders.background import BackgroundSequencer
from ansiscape.encoders.blink import BlinkSequencer
from ansiscape.encoders.calligraphy import CalligraphySequencer
from ansiscape.encoders.conceal import ConcealSequencer
from ansiscape.encoders.font import FontSequencer
from ansiscape.encoders.foreground import ForegroundSequencer
from ansiscape.encoders.frame import FrameSequencer
from ansiscape.encoders.ideogram import IdeogramSequencer
from ansiscape.encoders.invert import InvertSequencer
from ansiscape.encoders.overline import OverlineSequencer
from ansiscape.encoders.proportional_spacing import ProportionalSpacingSequencer
from ansiscape.encoders.sequencer import Sequencer
from ansiscape.encoders.strike import StrikeSequencer
from ansiscape.encoders.underline import UnderlineSequencer
from ansiscape.encoders.weight import WeightSequencer
from ansiscape.enums import InterpretationKey

encoders: Dict[InterpretationKey, Sequencer[Any]] = {
    InterpretationKey.BACKGROUND: BackgroundSequencer(),
    InterpretationKey.BLINK: BlinkSequencer(),
    InterpretationKey.CALLIGRAPHY: CalligraphySequencer(),
    InterpretationKey.CONCEAL: ConcealSequencer(),
    InterpretationKey.FONT: FontSequencer(),
    InterpretationKey.FOREGROUND: ForegroundSequencer(),
    InterpretationKey.FRAME: FrameSequencer(),
    InterpretationKey.IDEOGRAM: IdeogramSequencer(),
    InterpretationKey.INVERT: InvertSequencer(),
    InterpretationKey.OVERLINE: OverlineSequencer(),
    InterpretationKey.PROPORTIONAL_SPACING: ProportionalSpacingSequencer(),
    InterpretationKey.STRIKE: StrikeSequencer(),
    InterpretationKey.UNDERLINE: UnderlineSequencer(),
    InterpretationKey.WEIGHT: WeightSequencer(),
}


def get_encoder(key: InterpretationKey) -> Sequencer[Any]:
    return encoders[key]


__all__ = [
    "BackgroundSequencer",
    "BlinkSequencer",
    "CalligraphySequencer",
    "ConcealSequencer",
    "FontSequencer",
    "ForegroundSequencer",
    "FrameSequencer",
    "IdeogramSequencer",
    "InvertSequencer",
    "OverlineSequencer",
    "ProportionalSpacingSequencer",
    "StrikeSequencer",
    "UnderlineSequencer",
    "WeightSequencer",
]
