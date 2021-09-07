from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class ItalicValue(SingleValue[bool]):
    def __init__(self, value: bool) -> None:
        super().__init__(InterpretationKey.ITALIC, value)
