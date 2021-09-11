from ansiscape.enums import Calligraphy, InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class CalligraphyValue(SingleValue[Calligraphy]):
    def __init__(self, value: Calligraphy) -> None:
        super().__init__(InterpretationKey.CALLIGRAPHY, value)
