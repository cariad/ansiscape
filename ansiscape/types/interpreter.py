from typing import Generic, List, Protocol, Tuple

from ansiscape.enums import SelectGraphicRendition
from ansiscape.enums.interpretation_key import InterpretationKey
from ansiscape.types.attributes import Attributes
from ansiscape.types.interpretation_dict import InterpretationDict
from ansiscape.types.interpretation_value import TInterpretableValue
from ansiscape.types.sequence_protocol import SequencePart, SequenceProtocol
from ansiscape.types.sequencer_result import SequencerResult


class InterpreterProtocol(Protocol, Generic[TInterpretableValue]):
    @property
    def key(self) -> InterpretationKey:
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

    def sequence(self, stack: List[InterpretationDict]) -> SequencerResult:
        ...
