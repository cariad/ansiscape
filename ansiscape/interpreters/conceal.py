from typing import List

from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class ConcealInterpreter(Interpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change text visibility.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                8: True,
                28: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["conceal"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
