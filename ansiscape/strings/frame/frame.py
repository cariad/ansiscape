from abc import abstractproperty

from ansiscape.enums import Frame, InterpretationSpecial
from ansiscape.strings.sequence import Sequence
from ansiscape.types import InterpretationDict


class FrameStringWithCodes(Sequence):
    @abstractproperty
    def frame(self) -> Frame:
        """Gets the frame."""

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict(frame=self.frame)

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict(frame=InterpretationSpecial.REVERT)