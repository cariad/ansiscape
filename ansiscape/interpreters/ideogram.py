from typing import List

from ansiscape.enums import Ideogram
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class IdeogramInterpreter(GenericLookupInterpreter[Ideogram]):
    """
    Recognises and interprets ANSI escape codes that change ideogram formatting.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Ideogram.NONE,
                60: Ideogram.LINE_UNDER_OR_RIGHT,
                61: Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT,
                62: Ideogram.LINE_OVER_OR_LEFT,
                63: Ideogram.DOUBLE_LINE_OVER_OR_LEFT,
                64: Ideogram.STRESS,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """
        Updates `interpretation` to describe the given ideogram formatting.
        """

        interpretation["ideogram"] = self.attributes[code[0]]
