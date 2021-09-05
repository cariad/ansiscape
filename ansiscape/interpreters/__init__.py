from typing import List

from ansiscape.interpreters.intensity import IntensityInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.italic import ItalicInterpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter] = [
    IntensityInterpreter(),
    ItalicInterpreter(),
    VerticalPositionInterpreter(),
]

__all__ = [
    "IntensityInterpreter",
    "InterpretationDict",
    "interpreters",
    "ItalicInterpreter",
    "VerticalPositionInterpreter",
]
