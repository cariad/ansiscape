from abc import abstractproperty

from ansiscape.enums import InterpretationSpecial, Weight
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class WeightStringWithCodes(StringWithCodes):
    @abstractproperty
    def weight(self) -> Weight:
        ...

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(weight=self.weight)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(weight=InterpretationSpecial.REVERT)
