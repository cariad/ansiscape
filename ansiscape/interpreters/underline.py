from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Underline
from ansiscape.interpreter import Interpreter


class UnderlineValue(Interpreter[Underline]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.UNDERLINE,
            lookup={
                SelectGraphicRendition.DEFAULT: Underline.NONE,
                SelectGraphicRendition.UNDERLINE_SINGLE: Underline.SINGLE,
                SelectGraphicRendition.UNDERLINE_DOUBLE: Underline.DOUBLE,
                SelectGraphicRendition.UNDERLINE_NONE: Underline.NONE,
            },
        )
