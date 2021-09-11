from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class ProportionalSpacing(Sequence):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(proportional_spacing=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(proportional_spacing=InterpretationSpecial.REVERT)
