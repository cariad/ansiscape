from typing import Any, Dict, List, Union

from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.sequencers.background import BackgroundSequencer
from ansiscape.sequencers.blink import BlinkSequencer
from ansiscape.sequencers.calligraphy import CalligraphySequencer
from ansiscape.sequencers.conceal import ConcealSequencer
from ansiscape.sequencers.font import FontSequencer
from ansiscape.sequencers.foreground import ForegroundSequencer
from ansiscape.sequencers.frame import FrameSequencer
from ansiscape.sequencers.ideogram import IdeogramSequencer
from ansiscape.sequencers.invert import InvertSequencer
from ansiscape.sequencers.overline import OverlineSequencer
from ansiscape.sequencers.proportional_spacing import ProportionalSpacingSequencer
from ansiscape.sequencers.sequencer import Sequencer
from ansiscape.sequencers.strike import StrikeSequencer
from ansiscape.sequencers.underline import UnderlineSequencer
from ansiscape.sequencers.weight import WeightSequencer
from ansiscape.types import Attributes, InterpretationDict

sequencers: Dict[InterpretationKey, Sequencer[Any]] = {
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


def to_string(*args: Union[str, InterpretationDict]) -> str:
    wip = ""
    history: List[InterpretationDict] = []
    for arg in args:
        if isinstance(arg, str):
            wip += arg
        else:
            if not arg:
                # Don't add empty dictionaries.
                continue
            seq = sequence(interpretation=arg, history=history)
            wip += seq
            history.append(arg)

    return wip


def sequence(
    interpretation: InterpretationDict,
    history: List[InterpretationDict],
) -> str:
    sequences: List[Attributes] = [[]]

    for key in interpretation:
        if interpretation.get(key, None) is None:
            continue

        interpretation_key = InterpretationKey(key)
        sequencer = sequencers[interpretation_key]
        stack = [*history, interpretation]
        result = sequencer.sequence(stack)

        sgr = result.get("sgr", SelectGraphicRendition.DEFAULT)
        additional = result.get("additional", None) or []

        seq: List[int] = [sgr.value, *additional]

        if result.get("must_isolate", False):
            sequences.append(seq)
        else:
            sequences[0].extend(seq)

    return "".join([sequence_attributes(attrs) for attrs in sequences])


def sequence_attributes(attrs: Attributes) -> str:
    return f"\033[{';'.join([str(attr) for attr in attrs])}m"


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
