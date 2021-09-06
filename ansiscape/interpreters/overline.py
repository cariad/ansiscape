from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class OverlineInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change text overline.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                53: True,
                55: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given overline."""

        interpretation["overline"] = self.attributes[code[0]]
