from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class InvertValue(DictValue[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.INVERT,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.INVERT_ON: True,
                SelectGraphicRendition.INVERT_OFF: False,
            },
        )
