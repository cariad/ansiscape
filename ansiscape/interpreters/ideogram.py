from ansiscape.enums import Ideogram, InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class IdeogramValue(SingleValue[Ideogram]):
    def __init__(self, value: Ideogram) -> None:
        super().__init__(InterpretationKey.IDEOGRAM, value)
