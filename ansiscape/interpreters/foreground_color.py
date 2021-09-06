from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters.color_interpreter import ColorInterpreter
from ansiscape.types import Color, InterpretationDict


class ForegroundColorInterpreter(ColorInterpreter):
    """
    Recognises and interprets ANSI escape codes that change the foreground
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
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
            },
            color_index_offset=30,
        )

    def set_color(self, interpretation: InterpretationDict, color: Color) -> None:
        interpretation["foreground_color"] = color
