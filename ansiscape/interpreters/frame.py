from typing import List

from ansiscape.enums import Frame
from ansiscape.interpreters.generic_lookup_interpreter import GenericLookupInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict


class FrameInterpreter(GenericLookupInterpreter[Frame]):
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

    def update(self, code: List[int], interpretation: InterpretationDict) -> None:
        """Updates `interpretation` to describe the given framing."""

        interpretation["frame"] = self.attributes[code[0]]
