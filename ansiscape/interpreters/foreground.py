from ansiscape.enums import (
    InterpretationKey,
    MetaColor,
    NamedColor,
    SelectGraphicRendition,
)
from ansiscape.interpreters.color import ColorInterpreter


class ForegroundValue(ColorInterpreter):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.FOREGROUND,
            lookup={
                SelectGraphicRendition.DEFAULT: MetaColor.DEFAULT,
                SelectGraphicRendition.FOREGROUND_BLACK: NamedColor.BLACK,
                SelectGraphicRendition.FOREGROUND_BLUE: NamedColor.BLUE,
                SelectGraphicRendition.FOREGROUND_CYAN: NamedColor.CYAN,
                SelectGraphicRendition.FOREGROUND_DEFAULT: MetaColor.DEFAULT,
                SelectGraphicRendition.FOREGROUND_GREEN: NamedColor.GREEN,
                SelectGraphicRendition.FOREGROUND_MAGENTA: NamedColor.MAGENTA,
                SelectGraphicRendition.FOREGROUND_RED: NamedColor.RED,
                SelectGraphicRendition.FOREGROUND_WHITE: NamedColor.WHITE,
                SelectGraphicRendition.FOREGROUND_YELLOW: NamedColor.YELLOW,
            },
            rgb=SelectGraphicRendition.FOREGROUND_RGB,
        )
