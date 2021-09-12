from ansiscape.enums import Ideogram, InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class IdeogramValue(DictValue[Ideogram]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.IDEOGRAM,
            lookup={
                SelectGraphicRendition.DEFAULT: Ideogram.NONE,
                SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_OVER_OR_LEFT: Ideogram.SINGLE_LINE_OVER_OR_LEFT,
                SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_UNDER_OR_RIGHT: Ideogram.SINGLE_LINE_UNDER_OR_RIGHT,
                SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT: Ideogram.DOUBLE_LINE_OVER_OR_LEFT,
                SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT: Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT,
                SelectGraphicRendition.IDEOGRAM_NONE: Ideogram.NONE,
                SelectGraphicRendition.IDEOGRAM_STRESS: Ideogram.STRESS,
            },
        )
