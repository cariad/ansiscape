from ansiscape.enums import Font, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class FontValue(Interpreter[Font]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.FONT,
            lookup={
                SelectGraphicRendition.DEFAULT: Font.DEFAULT,
                SelectGraphicRendition.FONT_ALT_0: Font.ALT_0,
                SelectGraphicRendition.FONT_ALT_1: Font.ALT_1,
                SelectGraphicRendition.FONT_ALT_2: Font.ALT_2,
                SelectGraphicRendition.FONT_ALT_3: Font.ALT_3,
                SelectGraphicRendition.FONT_ALT_4: Font.ALT_4,
                SelectGraphicRendition.FONT_ALT_5: Font.ALT_5,
                SelectGraphicRendition.FONT_ALT_6: Font.ALT_6,
                SelectGraphicRendition.FONT_ALT_7: Font.ALT_7,
                SelectGraphicRendition.FONT_ALT_8: Font.ALT_8,
                SelectGraphicRendition.FONT_DEFAULT: Font.DEFAULT,
            },
        )
