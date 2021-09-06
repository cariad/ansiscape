from typing import List

from ansiscape.interpreters.blink_speed import BlinkSpeedInterpreter
from ansiscape.interpreters.conceal import ConcealInterpreter
from ansiscape.interpreters.intensity import IntensityInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.invert import InvertInterpreter
from ansiscape.interpreters.italic import ItalicInterpreter
from ansiscape.interpreters.strike import StrikeInterpreter
from ansiscape.interpreters.underline import UnderlineInterpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter] = [
    BlinkSpeedInterpreter(),
    ConcealInterpreter(),
    IntensityInterpreter(),
    InvertInterpreter(),
    ItalicInterpreter(),
    StrikeInterpreter(),
    UnderlineInterpreter(),
    VerticalPositionInterpreter(),
]

__all__ = [
    "BlinkSpeedInterpreter",
    "ConcealInterpreter",
    "IntensityInterpreter",
    "InterpretationDict",
    "interpreters",
    "InvertInterpreter",
    "ItalicInterpreter",
    "StrikeInterpreter",
    "UnderlineInterpreter",
    "VerticalPositionInterpreter",
]
