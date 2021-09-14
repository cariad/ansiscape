from functools import cached_property
from typing import Dict, List, Tuple, Union, cast

from ansiscape.enums import (
    InterpretationKey,
    InterpretationSpecial,
    SelectGraphicRendition,
)
from ansiscape.sequence import Sequence
from ansiscape.types import (
    Attributes,
    InterpretationDict,
    InterpreterProtocol,
    SequencePart,
    SequenceProtocol,
    SequencerResult,
    TInterpretableValue,
    UntypedInterpretation,
)


class Interpreter(InterpreterProtocol[TInterpretableValue]):
    def __init__(
        self,
        key: InterpretationKey,
        lookup: Dict[SelectGraphicRendition, TInterpretableValue],
    ) -> None:
        self._key = key
        self.lookup = lookup

    @cached_property
    def key(self) -> str:
        return str(self._key.value)

    @property
    def supported_codes(self) -> List[SelectGraphicRendition]:
        return [sgr for sgr in self.lookup]

    def from_attributes(
        self,
        attrs: Attributes,
    ) -> Tuple[TInterpretableValue, int]:
        """Gets the interpreted value and quantity of attributes claimed."""

        if not attrs:
            raise ValueError("attributes list is empty")

        try:
            sgr = SelectGraphicRendition(attrs[0])
        except Exception:
            raise
        if sgr in self.lookup:
            return self.lookup[sgr], 0
        return self.from_extended_attributes(attrs[1:])

    def from_extended_attributes(
        self,
        attrs: Attributes,
    ) -> Tuple[TInterpretableValue, int]:
        """Override to implement."""
        raise NotImplementedError()

    def make_sequence(
        self, value: TInterpretableValue, *parts: SequencePart
    ) -> Sequence:
        return Sequence(
            self.make_interpretation(value),
            *parts,
            self.make_interpretation(InterpretationSpecial.REVERT),
        )

    def make_sequence_from_attributes(
        self,
        attrs: Attributes,
        *parts: SequencePart,
    ) -> SequenceProtocol:
        value = self.from_attributes(attrs)
        return self.make_sequence(value[0], *parts)

    def make_interpretation(
        self,
        value: Union[TInterpretableValue, InterpretationSpecial],
    ) -> InterpretationDict:
        return cast(InterpretationDict, {self.key: value})

    def to_code(self, value: TInterpretableValue) -> SequencerResult:
        """Resolves a value into a sequencer result."""

        for sgr in self.lookup:
            if sgr == SelectGraphicRendition.DEFAULT:
                # We want to return something more specific than "everything".
                continue
            if self.lookup[sgr] == value:
                return SequencerResult(sgr=sgr)

        return self.get_extended_code(value)

    def get_extended_code(self, value: TInterpretableValue) -> SequencerResult:
        raise NotImplementedError()

    @property
    def off(self) -> SelectGraphicRendition:
        off_value = self.lookup[SelectGraphicRendition.DEFAULT]
        for sgr in self.lookup:
            if sgr == SelectGraphicRendition.DEFAULT:
                continue
            if self.lookup[sgr] != off_value:
                continue

            if type(self.lookup[sgr]) != type(off_value):
                continue

            return sgr

        raise ValueError("no off")

    def find_reversion(
        self,
        stack: List[UntypedInterpretation],
        index: int,
    ) -> SequencerResult:
        """
        Generates a sequence for the interpretation at the top of the stack. The
        lower stack comes into play only if the top item is a reversion.
        """

        index -= 1

        # Caching the key down here saves some trips. The profiler confirms it!
        key = self.key
        reversion_count = 0

        while index >= 0:
            top = stack[index]
            index -= 1

            if key not in top:
                continue

            value = top[key]

            # "type()" is faster than "isinstance()", but doesn't accommodate
            # inherited types.
            if type(value) is InterpretationSpecial:
                # We're nested inside another reversion.
                reversion_count -= 1
                continue

            if value is not None:
                if reversion_count == 1:
                    # Taking into account all the nested reversions and values we
                    # found along the way, we've finally reverted the change we came
                    # in here to look for.
                    return self.to_code(value)  # type: ignore

                reversion_count += 1

        return SequencerResult(sgr=self.off)
