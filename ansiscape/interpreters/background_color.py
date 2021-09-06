from ansiscape.enums import ColorType, StandardColor
from ansiscape.interpreters.color_interpreter import ColorInterpreter
from ansiscape.types import Color, InterpretationDict


class BackgroundColorInterpreter(ColorInterpreter):
    """
    Recognises and interprets ANSI escape codes that change the background
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                40: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BLACK,
                    ),
                ),
                41: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.RED,
                    ),
                ),
                42: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.GREEN,
                    ),
                ),
                43: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.YELLOW,
                    ),
                ),
                44: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BLUE,
                    ),
                ),
                45: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.MAGENTA,
                    ),
                ),
                46: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.CYAN,
                    ),
                ),
                47: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.WHITE,
                    ),
                ),
                48: (ColorType.EXTENDED, None),
                49: (
                    ColorType.DEFAULT,
                    Color(
                        color_type=ColorType.DEFAULT,
                        rgba=None,
                        standard_color=None,
                    ),
                ),
                100: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_BLACK,
                    ),
                ),
                101: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_RED,
                    ),
                ),
                102: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_GREEN,
                    ),
                ),
                103: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_YELLOW,
                    ),
                ),
                104: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_BLUE,
                    ),
                ),
                105: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_MAGENTA,
                    ),
                ),
                106: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_CYAN,
                    ),
                ),
                107: (
                    ColorType.STANDARD,
                    Color(
                        color_type=ColorType.STANDARD,
                        rgba=None,
                        standard_color=StandardColor.BRIGHT_WHITE,
                    ),
                ),
            },
            color_index_offset=40,
        )

    def set_color(self, interpretation: InterpretationDict, color: Color) -> None:
        interpretation["background_color"] = color
