from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class Sequence(StringWithCodes):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict()

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict()
