from typing import List

from ansiscape.enums import VerticalPosition
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class VerticalPositionInterpreter(GenericLookupInterpreter[VerticalPosition]):
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

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given vertical position."""

        interpretation["vertical_position"] = self.attributes[code[0]]
