from ansiscape.enums import Calligraphy, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class CalligraphyValue(Interpreter[Calligraphy]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.CALLIGRAPHY,
            lookup={
                SelectGraphicRendition.DEFAULT: Calligraphy.NONE,
                SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER: Calligraphy.BLACKLETTER,
                SelectGraphicRendition.CALLIGRAPHY_ITALIC: Calligraphy.ITALIC,
                SelectGraphicRendition.CALLIGRAPHY_NONE: Calligraphy.NONE,
            },
        )
