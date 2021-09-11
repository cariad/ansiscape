from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class ProportionalSpacing(StringWithCodes):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(proportional_spacing=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(proportional_spacing=InterpretationSpecial.REVERT)
