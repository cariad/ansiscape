from typing import List

from ansiscape.enums import Ideogram
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class IdeogramInterpreter(Interpreter[Ideogram]):
    """
    Recognises and interprets ANSI escape codes that change ideogram formatting.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Ideogram.NONE,
                60: Ideogram.LINE_UNDER_OR_RIGHT,
                61: Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT,
                62: Ideogram.LINE_OVER_OR_LEFT,
                63: Ideogram.DOUBLE_LINE_OVER_OR_LEFT,
                64: Ideogram.STRESS,
                65: Ideogram.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["ideogram"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
