from typing import List

from ansiscape.interpreters.blink_speed import BlinkSpeedInterpreter
from ansiscape.interpreters.intensity import IntensityInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.italic import ItalicInterpreter
from ansiscape.interpreters.underline import UnderlineInterpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter] = [
    BlinkSpeedInterpreter(),
    IntensityInterpreter(),
    ItalicInterpreter(),
    UnderlineInterpreter(),
    VerticalPositionInterpreter(),
]

__all__ = [
    "BlinkSpeedInterpreter",
    "IntensityInterpreter",
    "InterpretationDict",
    "interpreters",
    "ItalicInterpreter",
    "UnderlineInterpreter",
    "VerticalPositionInterpreter",
]
