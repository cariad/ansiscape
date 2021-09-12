from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class ConcealValue(DictValue[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.CONCEAL,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.CONCEAL_ON: True,
                SelectGraphicRendition.CONCEAL_OFF: False,
            },
        )
