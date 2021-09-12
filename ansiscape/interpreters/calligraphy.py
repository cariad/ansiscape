from ansiscape.enums import Calligraphy, InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class CalligraphyValue(DictValue[Calligraphy]):
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
