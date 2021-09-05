from typing import List

from ansiscape.enums import BlinkSpeed
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class BlinkSpeedInterpreter(GenericLookupInterpreter[BlinkSpeed]):
    """
    Recognises and interprets ANSI escape codes that change blink speed.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: BlinkSpeed.NONE,
                5: BlinkSpeed.SLOW,
                6: BlinkSpeed.FAST,
                25: BlinkSpeed.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given blink speed."""

        interpretation["blink_speed"] = self.attributes[code[0]]
