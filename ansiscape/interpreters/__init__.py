from typing import List

from ansiscape.interpreters.blackletter import BlackletterInterpreter
from ansiscape.interpreters.blink_speed import BlinkSpeedInterpreter
from ansiscape.interpreters.conceal import ConcealInterpreter
from ansiscape.interpreters.font_face import FontFaceInterpreter
from ansiscape.interpreters.frame import FrameInterpreter
from ansiscape.interpreters.intensity import IntensityInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.invert import InvertInterpreter
from ansiscape.interpreters.italic import ItalicInterpreter
from ansiscape.interpreters.proportional_spacing import ProportionalSpacingInterpreter
from ansiscape.interpreters.strike import StrikeInterpreter
from ansiscape.interpreters.underline import UnderlineInterpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter] = [
    BlackletterInterpreter(),
    BlinkSpeedInterpreter(),
    ConcealInterpreter(),
    FontFaceInterpreter(),
    FrameInterpreter(),
    IntensityInterpreter(),
    InvertInterpreter(),
    ItalicInterpreter(),
    ProportionalSpacingInterpreter(),
    StrikeInterpreter(),
    UnderlineInterpreter(),
    VerticalPositionInterpreter(),
]

__all__ = [
    "BlackletterInterpreter",
    "BlinkSpeedInterpreter",
    "ConcealInterpreter",
    "FontFaceInterpreter",
    "FrameInterpreter",
    "IntensityInterpreter",
    "InterpretationDict",
    "interpreters",
    "InvertInterpreter",
    "ItalicInterpreter",
    "ProportionalSpacingInterpreter",
    "StrikeInterpreter",
    "UnderlineInterpreter",
    "VerticalPositionInterpreter",
]
