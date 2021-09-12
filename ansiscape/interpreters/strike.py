from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class StrikeValue(DictValue[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.STRIKE,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.STRIKE_ON: True,
                SelectGraphicRendition.STRIKE_OFF: False,
            },
        )
