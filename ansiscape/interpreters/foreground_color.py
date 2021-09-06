from typing import List, Optional, Tuple

from ansiscape.b8 import get_8_bit_rgb
from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.types import Color, InterpretationDict


class ForegroundColorInterpreter(Interpreter[Tuple[ColorType, Optional[Color]]]):
    """
    Recognises and interprets ANSI escape codes that change the foreground
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                0: (
                    ColorType.DEFAULT,
                    Color(
                        color_type=ColorType.DEFAULT,
                        rgb=None,
                        standard_color=None,
                    ),
                ),
                30: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BLACK,
                    ),
                ),
                31: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.RED,
                    ),
                ),
                32: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.GREEN,
                    ),
                ),
                33: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.YELLOW,
                    ),
                ),
                34: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BLUE,
                    ),
                ),
                35: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.MAGENTA,
                    ),
                ),
                36: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.CYAN,
                    ),
                ),
                37: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.WHITE,
                    ),
                ),
                38: (
                    ColorType.EXTENDED,
                    None,
                ),
                90: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_BLACK,
                    ),
                ),
                91: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_RED,
                    ),
                ),
                92: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_GREEN,
                    ),
                ),
                93: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_YELLOW,
                    ),
                ),
                94: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_BLUE,
                    ),
                ),
                95: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_MAGENTA,
                    ),
                ),
                96: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_CYAN,
                    ),
                ),
                97: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgb=None,
                        standard_color=StandardColor.BRIGHT_WHITE,
                    ),
                ),
            }
        )

    def update(self, code: List[int], interpretation: InterpretationDict) -> int:
        """
        Updates `interpretation` to describe the ANSI escape code attribute at
        the start of the list.

        Returns the count of attributes that were interpreted.
        """

        try:
            color_type = self.attributes[code[0]][0]
            color = self.attributes[code[0]][1]
        except KeyError:
            return 0

        if color_type in [ColorType.DEFAULT, ColorType.STANDARD]:
            interpretation["foreground_color"] = color
            return 1

        if len(code) < 3:
            raise Exception("insufficient attributes for extended color")

        if code[1] == 5:
            # 8-bit colour:
            if 0 <= code[2] <= 7:
                # Actually, it's just a standard colour:
                interpretation["foreground_color"] = self.attributes[code[2] + 30][1]
                return 3
            if 8 <= code[2] <= 15:
                # Actually, it's just a standard bright colour:
                interpretation["foreground_color"] = self.attributes[code[2] + 82][1]
                return 3
            if 16 <= code[2] <= 231:
                interpretation["foreground_color"] = Color(
                    color_type=ColorType.EXTENDED,
                    rgb=get_8_bit_rgb(code[2]),
                    standard_color=None,
                )
                return 3

        raise Exception("unhandled extended color")
