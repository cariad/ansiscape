from ansiscape.enums import (
    ColorSpecial,
    InterpretationKey,
    SelectGraphicRendition,
    StandardColor,
)
from ansiscape.interpreters.color_value import ColorValue


class BackgroundValue(ColorValue):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.BACKGROUND,
            lookup={
                SelectGraphicRendition.DEFAULT: ColorSpecial.DEFAULT,
                SelectGraphicRendition.BACKGROUND_BLACK: StandardColor.BLACK,
                SelectGraphicRendition.BACKGROUND_BLUE: StandardColor.BLUE,
                SelectGraphicRendition.BACKGROUND_CYAN: StandardColor.CYAN,
                SelectGraphicRendition.BACKGROUND_DEFAULT: ColorSpecial.DEFAULT,
                SelectGraphicRendition.BACKGROUND_GREEN: StandardColor.GREEN,
                SelectGraphicRendition.BACKGROUND_MAGENTA: StandardColor.MAGENTA,
                SelectGraphicRendition.BACKGROUND_RED: StandardColor.RED,
                SelectGraphicRendition.BACKGROUND_WHITE: StandardColor.WHITE,
                SelectGraphicRendition.BACKGROUND_YELLOW: StandardColor.YELLOW,
            },
            rgb=SelectGraphicRendition.BACKGROUND_RGB,
        )
