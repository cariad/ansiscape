from typing import List

from ansiscape.enums import FontFace
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class FontFaceInterpreter(Interpreter[FontFace]):
    """
    Recognises and interprets ANSI escape codes that change the font face of
    subsequent text.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: FontFace.DEFAULT,
                10: FontFace.DEFAULT,
                11: FontFace.ALTERNATIVE_0,
                12: FontFace.ALTERNATIVE_1,
                13: FontFace.ALTERNATIVE_2,
                14: FontFace.ALTERNATIVE_3,
                15: FontFace.ALTERNATIVE_4,
                16: FontFace.ALTERNATIVE_5,
                17: FontFace.ALTERNATIVE_6,
                18: FontFace.ALTERNATIVE_7,
                19: FontFace.ALTERNATIVE_8,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            interpretation["font_face"] = self.attributes[code[0]]
            return 1
        except KeyError:
            return 0
