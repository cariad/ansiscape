from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class OverlineValue(DictValue[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.OVERLINE,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.OVERLINE_ON: True,
                SelectGraphicRendition.OVERLINE_OFF: False,
            },
        )
