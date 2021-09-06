from typing import List

from ansiscape.enums import Frame
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter


class FrameInterpreter(Interpreter[Frame]):
    """Recognises and interprets ANSI escape codes that change text framing."""

    def __init__(self) -> None:
        super().__init__(
            {
                0: Frame.NONE,
                51: Frame.FRAMED,
                52: Frame.ENCIRCLED,
                54: Frame.NONE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["frame"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
