from ansiscape.enums import InterpretationKey, Weight
from ansiscape.interpreters.single_value import SingleValue


class WeightValue(SingleValue[Weight]):
    def __init__(self, value: Weight) -> None:
        super().__init__(InterpretationKey.WEIGHT, value)
