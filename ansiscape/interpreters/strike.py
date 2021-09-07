from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class StrikeValue(SingleValue[bool]):
    def __init__(self, value: bool) -> None:
        super().__init__(InterpretationKey.STRIKE, value)
