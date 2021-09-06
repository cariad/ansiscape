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
                        rgba=None,
                        standard_color=None,
                    ),
                ),
                30: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BLACK,
                    ),
                ),
                31: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.RED,
                    ),
                ),
                32: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.GREEN,
                    ),
                ),
                33: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.YELLOW,
                    ),
                ),
                34: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BLUE,
                    ),
                ),
                35: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.MAGENTA,
                    ),
                ),
                36: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.CYAN,
                    ),
                ),
                37: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.WHITE,
                    ),
                ),
                38: (
                    ColorType.EXTENDED,
                    None,
                ),
                39: (
                    ColorType.DEFAULT,
                    Color(
                        color_type=ColorType.DEFAULT,
                        rgba=None,
                        standard_color=None,
                    ),
                ),
                90: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_BLACK,
                    ),
                ),
                91: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_RED,
                    ),
                ),
                92: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_GREEN,
                    ),
                ),
                93: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_YELLOW,
                    ),
                ),
                94: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_BLUE,
                    ),
                ),
                95: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_MAGENTA,
                    ),
                ),
                96: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_CYAN,
                    ),
                ),
                97: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
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

        if code[1] == 0:
            raise NotImplementedError("no implementation defined")

        if code[1] == 1:
            # Transparent:
            interpretation["foreground_color"] = Color(
                color_type=ColorType.EXTENDED,
                rgba=(0.0, 0.0, 0.0, 0.0),
                standard_color=None,
            )
            return 2

        if code[1] == 2:
            # 24-bit colour:
            #
            # At this point, the arguments are _so_ fluid that we have to assume
            # the entire set is up for grabs, and none are intended for
            # subsequent interpreters.

            #     "38;2"
            #     "38;2;<colour-space>"
            #
            # We don't support colour spaces (yet). R, G and B are optional,
            # so this is weirdly okay. We'll just intentionally make no
            # change.

            if len(code) == 4:
                raise Exception(f"unexpected attributes: {code}")

            elif len(code) == 5:
                #     "38;2;<r>;<g>;<b>"
                interpretation["foreground_color"] = Color(
                    color_type=ColorType.EXTENDED,
                    rgba=(code[2] / 255, code[3] / 255, code[4] / 255, 1.0),
                    standard_color=None,
                )

            elif len(code) >= 6:
                #     "38;2;<colour-space>;<r>;<g>;<b>;<more-unsupported>"
                #
                # We don't support colour spaces (yet).
                interpretation["foreground_color"] = Color(
                    color_type=ColorType.EXTENDED,
                    rgba=(code[3] / 255, code[4] / 255, code[5] / 255, 1.0),
                    standard_color=None,
                )

            return len(code)

        if code[1] == 3:
            raise NotImplementedError("Cyan-Magenta-Yellow schema not supported")

        if code[1] == 4:
            raise NotImplementedError("Cyan-Magenta-Yellow-Black schema not supported")

        if code[1] == 5:
            # 8-bit colour:
            if not 0 <= code[2] <= 255:
                raise ValueError(f"argument [2] ({code[2]}) must be 0-255 inclusive")

            if 0 <= code[2] <= 7:
                # Actually, it's just a standard colour:
                interpretation["foreground_color"] = self.attributes[code[2] + 30][1]

            elif 8 <= code[2] <= 15:
                # Actually, it's just a standard bright colour:
                interpretation["foreground_color"] = self.attributes[code[2] + 82][1]

            else:
                # 8-bit RGB look-up:
                interpretation["foreground_color"] = Color(
                    color_type=ColorType.EXTENDED,
                    rgba=(*get_8_bit_rgb(code[2]), 1.0),
                    standard_color=None,
                )

            return 3

        raise Exception("unhandled extended color")
