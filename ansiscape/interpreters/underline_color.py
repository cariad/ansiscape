from ansiscape.enums import ColorType
from ansiscape.interpreters.color_interpreter import ColorInterpreter
from ansiscape.types import Color, InterpretationDict


class UnderlineColorInterpreter(ColorInterpreter):
    """
    Recognises and interprets ANSI escape codes that change the underline
    colour.
    """

    def __init__(self) -> None:
        super().__init__(
            {
                58: (ColorType.EXTENDED, None),
                59: (
                    ColorType.DEFAULT,
                    Color(
                        color_type=ColorType.DEFAULT,
                        rgba=None,
                        standard_color=None,
                    ),
                ),
            },
        )

    def set_color(self, interpretation: InterpretationDict, color: Color) -> None:
        interpretation["underline_color"] = color
