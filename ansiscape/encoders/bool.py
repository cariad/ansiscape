from abc import abstractproperty
from typing import Optional

from ansiscape.encoders.sequencer import Sequencer
from ansiscape.enums import SelectGraphicRendition
from ansiscape.types import SequencerResult


class BoolSequencer(Sequencer[bool]):
    @abstractproperty
    def off(self) -> SelectGraphicRendition:
        """
        Gets the Select Graphic Rendition code that disables this state.
        """

    @abstractproperty
    def on(self) -> SelectGraphicRendition:
        """
        Gets the Select Graphic Rendition code that enables this state.
        """

    def resolve(self, value: Optional[bool]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        return SequencerResult(sgr=self.on if value else self.off)
