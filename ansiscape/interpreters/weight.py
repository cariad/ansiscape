from ansiscape.enums import InterpretationKey, Weight
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class WeightValue(DictValue[Weight]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.WEIGHT,
            lookup={
                SelectGraphicRendition.DEFAULT: Weight.NORMAL,
                SelectGraphicRendition.WEIGHT_HEAVY: Weight.HEAVY,
                SelectGraphicRendition.WEIGHT_LIGHT: Weight.LIGHT,
                SelectGraphicRendition.WEIGHT_NORMAL: Weight.NORMAL,
            },
        )
