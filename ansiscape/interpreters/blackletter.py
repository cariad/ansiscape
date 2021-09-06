from typing import List

from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class BlackletterInterpreter(Interpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change the blackletter of
    subsequent text.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                20: True,
                23: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["blackletter"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
