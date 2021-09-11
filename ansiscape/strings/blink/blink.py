from abc import abstractproperty

from ansiscape.enums import Blink
from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class BlinkStringWithCodes(Sequence):
    @abstractproperty
    def blink(self) -> Blink:
        """Gets the blink speed."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(blink=self.blink)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(blink=InterpretationSpecial.REVERT)
