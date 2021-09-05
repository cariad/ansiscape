from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class InvertInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change inversion.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                7: True,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given inversion."""

        interpretation["invert"] = self.attributes[code[0]]
