from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class ConcealInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change text visibility.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                8: True,
                28: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given italics."""

        interpretation["conceal"] = self.attributes[code[0]]
