from abc import abstractproperty

from ansiscape.enums import Font, InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class AlternateFont(Sequence):
    @abstractproperty
    def font(self) -> Font:
        """Gets the font."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(font=self.font)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(font=InterpretationSpecial.REVERT)
