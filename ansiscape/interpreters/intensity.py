from typing import List

from ansiscape.enums import Intensity
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class IntensityInterpreter(GenericLookupInterpreter[Intensity]):
    """
    Recognises and interprets ANSI escape codes that change text intensity.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Intensity.NORMAL,
                1: Intensity.BOLD,
                2: Intensity.DIM,
                22: Intensity.NORMAL,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given intensity."""

        interpretation["intensity"] = self.attributes[code[0]]
