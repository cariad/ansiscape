from typing import List

from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class OverlineInterpreter(Interpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change text overline.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                53: True,
                55: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["overline"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
