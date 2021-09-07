from ansiscape.enums import Blink, InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class BlinkValue(SingleValue[Blink]):
    def __init__(self, value: Blink) -> None:
        super().__init__(InterpretationKey.BLINK, value)
