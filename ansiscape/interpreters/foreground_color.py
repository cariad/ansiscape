from typing import List

from ansiscape.enums import StandardColor
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class ForegroundColorInterpreter(GenericLookupInterpreter[StandardColor]):
    """
    Recognises and interprets ANSI escape codes that change the foreground
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: StandardColor.DEFAULT,
                30: StandardColor.BLACK,
                31: StandardColor.RED,
                32: StandardColor.GREEN,
                33: StandardColor.YELLOW,
                34: StandardColor.BLUE,
                35: StandardColor.MAGENTA,
                36: StandardColor.CYAN,
                37: StandardColor.WHITE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given foreground colour."""

        interpretation["foreground_color"] = self.attributes[code[0]]
