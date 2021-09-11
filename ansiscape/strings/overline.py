from ansiscape.enums import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class Overline(Sequence):
    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(overline=True)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(overline=InterpretationSpecial.REVERT)