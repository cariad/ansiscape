from abc import abstractproperty
from typing import Dict, Optional

from ansiscape.sequencers.sequencer import Sequencer, TValue
from ansiscape.types import SequencerResult


class EnumSequencer(Sequencer[TValue]):
    @abstractproperty
    def lookup(self) -> Dict[Optional[TValue], SequencerResult]:
        """Gets the lookup dictionary."""

    def resolve(self, value: Optional[TValue]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        return self.lookup[value]
