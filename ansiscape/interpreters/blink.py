from ansiscape.enums import Blink, InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class BlinkValue(DictValue[Blink]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.BLINK,
            lookup={
                SelectGraphicRendition.DEFAULT: Blink.NONE,
                SelectGraphicRendition.BLINK_SLOW: Blink.SLOW,
                SelectGraphicRendition.BLINK_FAST: Blink.FAST,
                SelectGraphicRendition.BLINK_NONE: Blink.NONE,
            },
        )
