from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class Strike(StringWithCodes):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(strike=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(strike=InterpretationSpecial.REVERT)
