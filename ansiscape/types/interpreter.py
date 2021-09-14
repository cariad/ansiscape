from functools import cached_property
from typing import Generic, List, Protocol, Tuple

from ansiscape.enums import SelectGraphicRendition
from ansiscape.types.attributes import Attributes
from ansiscape.types.interpretation_dict import UntypedInterpretation
from ansiscape.types.interpretation_value import TInterpretableValue
from ansiscape.types.sequence_protocol import SequencePart, SequenceProtocol
from ansiscape.types.sequencer_result import SequencerResult


class InterpreterProtocol(Protocol, Generic[TInterpretableValue]):
    @cached_property
    def key(self) -> str:
        ...

    @property
    def supported_codes(self) -> List[SelectGraphicRendition]:
        ...

    def from_attributes(
        self,
        attrs: Attributes,
    ) -> Tuple[TInterpretableValue, int]:
        ...

    def make_sequence(
        self,
        value: TInterpretableValue,
        *parts: SequencePart,
    ) -> SequenceProtocol:
        ...

    def make_sequence_from_attributes(
        self,
        attrs: Attributes,
        *parts: SequencePart,
    ) -> SequenceProtocol:
        ...

    def find_reversion(
        self,
        stack: List[UntypedInterpretation],
        index: int,
    ) -> SequencerResult:
        ...

    def to_code(self, value: TInterpretableValue) -> SequencerResult:
        ...
