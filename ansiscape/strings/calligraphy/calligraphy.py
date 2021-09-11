from abc import abstractproperty

from ansiscape.enums import Calligraphy, InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class CalligraphyStringWithCodes(StringWithCodes):
    @abstractproperty
    def calligraphy(self) -> Calligraphy:
        ...

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(calligraphy=self.calligraphy)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(calligraphy=InterpretationSpecial.REVERT)
