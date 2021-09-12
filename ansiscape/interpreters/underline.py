from ansiscape.enums import InterpretationKey, Underline
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class UnderlineValue(DictValue[Underline]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.UNDERLINE,
            lookup={
                SelectGraphicRendition.DEFAULT: Underline.NONE,
                SelectGraphicRendition.UNDERLINE_SINGLE: Underline.SINGLE,
                SelectGraphicRendition.UNDERLINE_DOUBLE: Underline.DOUBLE,
                SelectGraphicRendition.UNDERLINE_NONE: Underline.NONE,
            },
        )
