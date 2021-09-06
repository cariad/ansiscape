from typing import List

from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class ProportionalSpacingInterpreter(GenericLookupInterpreter[bool]):
    """
    Recognises and interprets ANSI escape codes that change the proportional
    spacing of subsequent text.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: False,
                26: True,
                50: False,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """
        Updates `interpretation` to describe the given proportional spacing.
        """

        interpretation["proportional_spacing"] = self.attributes[code[0]]
