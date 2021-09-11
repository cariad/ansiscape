from abc import abstractproperty

from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.strings.string_with_codes import StringWithCodes
from ansiscape.types import InterpretationDict
from ansiscape.types.color import Color


class Foreground(StringWithCodes):
    @abstractproperty
    def color(self) -> Color:
        ...

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(foreground=self.color)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(foreground=InterpretationSpecial.REVERT)
