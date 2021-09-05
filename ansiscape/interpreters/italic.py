from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class ItalicInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change text italic.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                3: True,
                23: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given italics."""

        interpretation["italic"] = self.attributes[code[0]]
