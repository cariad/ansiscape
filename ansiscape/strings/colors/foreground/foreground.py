from abc import abstractproperty

from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict
from ansiscape.types.color import Color


class Foreground(Sequence):
    @abstractproperty
    def color(self) -> Color:
        """Gets the colour."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(foreground=self.color)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(foreground=InterpretationSpecial.REVERT)
