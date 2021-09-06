from typing import List

from ansiscape.enums import BlinkSpeed
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class BlinkSpeedInterpreter(Interpreter[BlinkSpeed]):
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

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["blink_speed"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
