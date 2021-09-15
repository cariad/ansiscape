from ansiscape.enums import InterpretationKey, SelectGraphicRendition, Weight
from ansiscape.interpreter import Interpreter


class WeightValue(Interpreter[Weight]):
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
