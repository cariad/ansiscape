from ansiscape.enums import (
    ColorSpecial,
    InterpretationKey,
    SelectGraphicRendition,
    StandardColor,
)
from ansiscape.interpreters.color_value import ColorValue


class ForegroundValue(ColorValue):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.FOREGROUND,
            lookup={
                SelectGraphicRendition.DEFAULT: ColorSpecial.DEFAULT,
                SelectGraphicRendition.FOREGROUND_BLACK: StandardColor.BLACK,
                SelectGraphicRendition.FOREGROUND_BLUE: StandardColor.BLUE,
                SelectGraphicRendition.FOREGROUND_CYAN: StandardColor.CYAN,
                SelectGraphicRendition.FOREGROUND_DEFAULT: ColorSpecial.DEFAULT,
                SelectGraphicRendition.FOREGROUND_GREEN: StandardColor.GREEN,
                SelectGraphicRendition.FOREGROUND_MAGENTA: StandardColor.MAGENTA,
                SelectGraphicRendition.FOREGROUND_RED: StandardColor.RED,
                SelectGraphicRendition.FOREGROUND_WHITE: StandardColor.WHITE,
                SelectGraphicRendition.FOREGROUND_YELLOW: StandardColor.YELLOW,
            },
            rgb=SelectGraphicRendition.FOREGROUND_RGB,
        )
