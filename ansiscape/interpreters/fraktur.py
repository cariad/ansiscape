from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class FrakturValue(SingleValue[bool]):
    def __init__(self, value: bool) -> None:
        super().__init__(InterpretationKey.FRACKTUR, value)
