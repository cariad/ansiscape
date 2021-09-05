from typing import Dict, List

from ansiscape.enums import VerticalPosition
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class VerticalPositionInterpreter(Interpreter):
    """
    Recognises and interprets ANSI escape codes that change text's vertical
    position.
    """

    def __init__(self) -> None:
        super().__init__()

        self.attributes: Dict[int, VerticalPosition] = {
            0: VerticalPosition.NONE,
            73: VerticalPosition.SUPERSCRIPT,
            74: VerticalPosition.SUBSCRIPT,
            75: VerticalPosition.NONE,
        }

    def claim(self, code: List[int]) -> int:
        """
        Returns the quantity of attributes at the start of the code that this
        interpreter wishes to claim.
        """

        return 1 if code[0] in self.attributes else 0

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given vertical position."""

        interpretation["vertical_position"] = self.attributes[code[0]]
