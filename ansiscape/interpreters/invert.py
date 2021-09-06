from typing import List

from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class InvertInterpreter(Interpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change inversion.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                7: True,
                27: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["invert"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
