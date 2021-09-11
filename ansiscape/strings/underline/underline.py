from abc import abstractproperty

from ansiscape.enums import InterpretationSpecial, Underline
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class UnderlineStringWithCodes(Sequence):
    @abstractproperty
    def underline(self) -> Underline:
        """Gets the underline."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(underline=self.underline)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(underline=InterpretationSpecial.REVERT)
