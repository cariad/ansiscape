from typing import Dict, List

from ansiscape.enums import Intensity
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class IntensityInterpreter(Interpreter):
    """
    Recognises and interprets ANSI escape codes that change text intensity.
    """

    def __init__(self) -> None:
        super().__init__()

        self.attributes: Dict[int, Intensity] = {
            0: Intensity.NORMAL,
            1: Intensity.BOLD,
            2: Intensity.DIM,
            22: Intensity.NORMAL,
        }

    def claim(self, code: List[int]) -> int:
        """
        Returns the quantity of attributes at the start of the code that this
        interpreter wishes to claim.
        """

        return 1 if code[0] in self.attributes else 0

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given intensity."""

        interpretation["intensity"] = self.attributes[code[0]]
