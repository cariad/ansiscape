from typing import Dict, List

from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class ItalicInterpreter(Interpreter):
    """
    Recognises and interprets ANSI escape codes that change text italic.
    """

    def __init__(self) -> None:
        super().__init__()

        self.attributes: Dict[int, bool] = {
            0: False,
            3: True,
            23: False,
        }

    def claim(self, code: List[int]) -> int:
        """
        Returns the quantity of attributes at the start of the code that this
        interpreter wishes to claim.
        """

        return 1 if code[0] in self.attributes else 0

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given italics."""

        interpretation["italic"] = self.attributes[code[0]]
