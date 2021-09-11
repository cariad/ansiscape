from abc import abstractproperty

from ansiscape.enums import Ideogram, InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class IdeogramStringWithCodes(StringWithCodes):
    @abstractproperty
    def ideogram(self) -> Ideogram:
        """Gets the ideogram."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(ideogram=self.ideogram)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(ideogram=InterpretationSpecial.REVERT)
