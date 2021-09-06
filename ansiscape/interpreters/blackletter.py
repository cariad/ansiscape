from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class BlackletterInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change the blackletter of
    subsequent text.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                20: True,
                23: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given blackletter."""

        interpretation["blackletter"] = self.attributes[code[0]]
