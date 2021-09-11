from abc import abstractproperty

from ansiscape.enums import Ideogram, InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class IdeogramStringWithCodes(Sequence):
    @abstractproperty
    def ideogram(self) -> Ideogram:
        """Gets the ideogram."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(ideogram=self.ideogram)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(ideogram=InterpretationSpecial.REVERT)
