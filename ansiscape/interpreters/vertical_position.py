from typing import List

from ansiscape.enums import VerticalPosition
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class VerticalPositionInterpreter(Interpreter[VerticalPosition]):
    """
    Recognises and interprets ANSI escape codes that change text vertical
    position.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: VerticalPosition.NONE,
                73: VerticalPosition.SUPERSCRIPT,
                74: VerticalPosition.SUBSCRIPT,
                75: VerticalPosition.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["vertical_position"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
