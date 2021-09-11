from abc import abstractproperty

from ansiscape.enums import InterpretationSpecial, Underline
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class UnderlineStringWithCodes(StringWithCodes):
    @abstractproperty
    def underline(self) -> Underline:
        ...

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(underline=self.underline)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(underline=InterpretationSpecial.REVERT)
