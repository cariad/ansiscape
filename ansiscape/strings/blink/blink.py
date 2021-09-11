from abc import abstractproperty

from ansiscape.enums import Blink
from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict


class BlinkStringWithCodes(StringWithCodes):
    @abstractproperty
    def blink(self) -> Blink:
        ...

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(blink=self.blink)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(blink=InterpretationSpecial.REVERT)
