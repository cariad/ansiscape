from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class Invert(Sequence):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(invert=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(invert=InterpretationSpecial.REVERT)
