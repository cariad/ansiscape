from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class ProportionalSpacingValue(DictValue[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.PROPORTIONAL_SPACING,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.PROPORTIONAL_SPACING_ON: True,
                SelectGraphicRendition.PROPORTIONAL_SPACING_OFF: False,
            },
        )
