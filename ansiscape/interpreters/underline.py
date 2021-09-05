from typing import List

from ansiscape.enums import Underline
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class UnderlineInterpreter(GenericLookupInterpreter[Underline]):
    """
    Recognises and interprets ANSI escape codes that change text intensity.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Underline.NONE,
                4: Underline.SINGLE,
                21: Underline.DOUBLE,
                24: Underline.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given underline."""

        interpretation["underline"] = self.attributes[code[0]]
