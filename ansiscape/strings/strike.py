from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class Strike(Sequence):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(strike=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(strike=InterpretationSpecial.REVERT)
