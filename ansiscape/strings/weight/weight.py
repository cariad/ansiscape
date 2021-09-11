from abc import abstractproperty

from ansiscape.enums import InterpretationSpecial, Weight
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class WeightStringWithCodes(Sequence):
    @abstractproperty
    def weight(self) -> Weight:
        """Gets the weight."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(weight=self.weight)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(weight=InterpretationSpecial.REVERT)
