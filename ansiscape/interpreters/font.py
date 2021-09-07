from ansiscape.enums import Font, InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class FontValue(SingleValue[Font]):
    def __init__(self, value: Font) -> None:
        super().__init__(InterpretationKey.FONT, value)
