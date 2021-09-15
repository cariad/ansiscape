from ansiscape.enums import (
    InterpretationKey,
    MetaColor,
    NamedColor,
    SelectGraphicRendition,
)
from ansiscape.interpreters.color import ColorInterpreter


class BackgroundValue(ColorInterpreter):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.BACKGROUND,
            lookup={
                SelectGraphicRendition.DEFAULT: MetaColor.DEFAULT,
                SelectGraphicRendition.BACKGROUND_BLACK: NamedColor.BLACK,
                SelectGraphicRendition.BACKGROUND_BLUE: NamedColor.BLUE,
                SelectGraphicRendition.BACKGROUND_CYAN: NamedColor.CYAN,
                SelectGraphicRendition.BACKGROUND_DEFAULT: MetaColor.DEFAULT,
                SelectGraphicRendition.BACKGROUND_GREEN: NamedColor.GREEN,
                SelectGraphicRendition.BACKGROUND_MAGENTA: NamedColor.MAGENTA,
                SelectGraphicRendition.BACKGROUND_RED: NamedColor.RED,
                SelectGraphicRendition.BACKGROUND_WHITE: NamedColor.WHITE,
                SelectGraphicRendition.BACKGROUND_YELLOW: NamedColor.YELLOW,
            },
            rgb=SelectGraphicRendition.BACKGROUND_RGB,
        )
