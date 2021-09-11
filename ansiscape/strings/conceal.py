from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class Conceal(Sequence):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(conceal=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(conceal=InterpretationSpecial.REVERT)
