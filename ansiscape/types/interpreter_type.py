from functools import cached_property
from typing import Generic, List, Protocol, Tuple

from ansiscape.types.attributes import Attributes
from ansiscape.types.interpretation import Interpretation
from ansiscape.types.interpretation_value import TInterpretableValue
from ansiscape.types.sequence_type import SequencePart, SequenceType
from ansiscape.types.sequencer_result import SequencerResult


class InterpreterType(Protocol, Generic[TInterpretableValue]):
    """
    Handles interpreration and translation of `TInterpretableValue` values.
    """

    def find_reversion(
        self,
        stack: List[Interpretation],
        index: int,
    ) -> SequencerResult:
        """
        Gets the Select Graphic Rendition attributes that represent the value
        for the reversion at `index` of `stack`.
        """

    def from_attributes(self, attrs: Attributes) -> Tuple[TInterpretableValue, int]:
        """
        Gets the interpreted value of the attribute at the end of the stack.
        Further attributes will be read only if needed to fullfill that
        attribute.

        Returns the interpreted value and the count of attributes claimed.
        """

    def interpret(self, attrs: Attributes, interpretation: Interpretation) -> int:
        """
        Populates `interpretation` with the interpretation of the attribute at
        the end of the stack. Further attributes will be read only if needed to
        fullfill that attribute.

        Returns the count of attributes claimed.
        """

    @cached_property
    def key(self) -> str:
        """
        Gets the key of `InterpretationDict` that this interpreter handles.
        """
        # This is intentionally a string rather the original enum value for
        # dictionary look-up performance.

    def make_sequence(
        self,
        value: TInterpretableValue,
        *parts: SequencePart,
    ) -> SequenceType:
        """
        Makes a sequence that wraps `parts` inside a terminating interpretation
        of `value`.
        """

    @cached_property
    def supported_codes(self) -> List[int]:
        """
        Gets the Select Graphic Rendition codes that this interpreter handles.
        """

    def to_code(self, value: TInterpretableValue) -> SequencerResult:
        """
        Resolves `value` into a sequence of Select Graphic Rendition attributes.
        """
