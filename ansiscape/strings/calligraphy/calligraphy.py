from abc import abstractproperty

from ansiscape.enums import Calligraphy, InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class CalligraphyStringWithCodes(Sequence):
    @abstractproperty
    def calligraphy(self) -> Calligraphy:
        """Gets the calligraphy."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(calligraphy=self.calligraphy)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(calligraphy=InterpretationSpecial.REVERT)
