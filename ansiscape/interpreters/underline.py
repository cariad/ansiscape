from typing import List

from ansiscape.enums import Underline
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class UnderlineInterpreter(Interpreter[Underline]):
    """
    Recognises and interprets ANSI escape codes that change text intensity.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Underline.NONE,
                4: Underline.SINGLE,
                21: Underline.DOUBLE,
                24: Underline.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["underline"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
