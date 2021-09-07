from ansiscape.enums import InterpretationKey, Underline
from ansiscape.interpreters.single_value import SingleValue


class UnderlineValue(SingleValue[Underline]):
    def __init__(self, value: Underline) -> None:
        super().__init__(InterpretationKey.UNDERLINE, value)
