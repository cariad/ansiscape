from typing import List

from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter] = [
    VerticalPositionInterpreter(),
]

__all__ = [
    "InterpretationDict",
    "interpreters",
    "VerticalPositionInterpreter",
]
