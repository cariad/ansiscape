from typing import List

from ansiscape.enums import Color
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import InterpretationDict


class ForegroundColorInterpreter(Interpreter[Color]):
    """
    Recognises and interprets ANSI escape codes that change the foreground
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: Color.DEFAULT,
                30: Color.BLACK,
                31: Color.RED,
                32: Color.GREEN,
                33: Color.YELLOW,
                34: Color.BLUE,
                35: Color.MAGENTA,
                36: Color.CYAN,
                37: Color.WHITE,
                38: Color.CUSTOM,
                90: Color.BRIGHT_BLACK,
                91: Color.BRIGHT_RED,
                92: Color.BRIGHT_GREEN,
                93: Color.BRIGHT_YELLOW,
                94: Color.BRIGHT_BLUE,
                95: Color.BRIGHT_MAGENTA,
                96: Color.BRIGHT_CYAN,
                97: Color.BRIGHT_WHITE,
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        if code[0] == 0:
            # Reset:
            interpretation["foreground_color"] = self.attributes[code[0]]
            return 1

        if 30 <= code[0] <= 37:
            # Standard colour:
            interpretation["foreground_color"] = self.attributes[code[0]]
            return 1

        if code[0] == 38:
            # Extended colour:
            if len(code) < 3:
                raise Exception("insufficient attributes for extended color")

            if code[1] == 5:
                # 8-bit colour:
                if 0 <= code[2] <= 7:
                    # Actually, it's just a standard colour:
                    interpretation["foreground_color"] = self.attributes[code[2] + 30]
                    return 3
                if 8 <= code[2] <= 15:
                    # Actually, it's just a standard bright colour:
                    interpretation["foreground_color"] = self.attributes[code[2] + 82]
                    return 3

            raise Exception("unhandled extended color")

        if 90 <= code[0] <= 97:
            # Standard bright colour:
            interpretation["foreground_color"] = self.attributes[code[0]]
            return 1

        return 0
