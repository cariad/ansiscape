from functools import cached_property
from typing import Dict, List, Tuple, Union, cast

from ansiscape.enums import (
    InterpretationKey,
    MetaInterpretation,
    SelectGraphicRendition,
)
from ansiscape.sequence import Sequence
from ansiscape.types import (
    Attributes,
    Interpretation,
    InterpreterType,
    SequencePart,
    SequencerResult,
    TInterpretableValue,
)


class Interpreter(InterpreterType[TInterpretableValue]):
    """
    Handles interpreration and translation of `TInterpretableValue` values.

    Arguments:
        key:    Key of `InterpretationDict` that this interpreter handles

        lookup: Dictionary of Select Graphic Rendition codes and known values
                to return for each
    """

    def __init__(
        self,
        key: InterpretationKey,
        lookup: Dict[SelectGraphicRendition, TInterpretableValue],
    ) -> None:
        self._key = key
        # Convert to integer keys for look-up performance.
        self.lookup = {k.value: v for (k, v) in lookup.items()}

    def find_reversion(
        self,
        stack: List[Interpretation],
        index: int,
    ) -> SequencerResult:
        """
        Gets the Select Graphic Rendition attributes that represent the value
        for the reversion at `index` of `stack`.
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

            # We can't normally pluck out of a typed dictionary with random
            # string keys, but we'll ask the linter to look the other way down
            # here for performance. This function gets pummelled.
            value: TInterpretableValue = top[key]  # type: ignore

            # "type()" is faster than "isinstance()", but doesn't accommodate
            # inherited types.
            if type(value) is MetaInterpretation:
                # We're nested inside another reversion.
                reversion_count -= 1
                continue

            # if value is not None:
            if reversion_count == 1:
                # Taking into account all the nested reversions and values we
                # found along the way, we've finally reverted the change we came
                # in here to look for.
                return self.to_code(value)

            reversion_count += 1

        return SequencerResult(attributes=[self.off])

    def from_attributes(self, attrs: Attributes) -> Tuple[TInterpretableValue, int]:
        """
        Gets the interpreted value of the attribute at the end of the stack.
        Further attributes will be read only if needed to fullfill that
        attribute.

        Returns the interpreted value and the count of attributes claimed.
        """

        if attrs[0] in self.lookup:
            return self.lookup[attrs[0]], 1

        value, claimed = self.from_extended_attributes(attrs[1:])
        return (value, claimed + 1)

    def from_extended_attributes(
        self,
        attrs: Attributes,
    ) -> Tuple[TInterpretableValue, int]:
        """
        Override to provide an interpretation for attributes not present in the
        look-up dictionary.

        Returns the interpreted value and the count of attributes claimed.
        """

    def interpret(self, attrs: Attributes, interpretation: Interpretation) -> int:
        """
        Populates `interpretation` with the interpretation of the attribute at
        the end of the stack. Further attributes will be read only if needed to
        fullfill that attribute.

        Returns the count of attributes claimed.
        """

        value, claimed = self.from_attributes(attrs)

        # We can't normally push into a typed dictionary with random string
        # keys, but we'll ask the linter to look the other way down here for
        # performance.
        interpretation[self.key] = value  # type: ignore
        return claimed

    @cached_property
    def key(self) -> str:
        """
        Gets the key of `InterpretationDict` that this interpreter handles.
        """

        # This is intentionally a string rather the original enum value for
        # dictionary look-up performance.
        return str(self._key.value)

    def make_sequence(
        self,
        value: Union[SelectGraphicRendition, TInterpretableValue],
        *parts: SequencePart,
    ) -> Sequence:
        """
        Makes a sequence that wraps `parts` inside a terminating interpretation
        of `value`.
        """

        if isinstance(value, SelectGraphicRendition):
            value, _ = self.from_attributes([value.value])

        return Sequence(
            cast(Interpretation, {self.key: value}),
            *parts,
            cast(Interpretation, {self.key: MetaInterpretation.REVERT}),
        )

    @property
    def off(self) -> int:
        """
        Gets the Select Graphic Rendition attribute that represents the
        disabling of this interpreter's state.
        """

        found = SelectGraphicRendition.DEFAULT.value
        off_value = self.lookup[SelectGraphicRendition.DEFAULT.value]

        for sgr in self.lookup:
            if sgr == SelectGraphicRendition.DEFAULT.value:
                continue
            if self.lookup[sgr] != off_value:
                continue
            if type(self.lookup[sgr]) != type(off_value):
                continue

            found = sgr
            break

        return found

    @cached_property
    def supported_codes(self) -> List[int]:
        """
        Gets the Select Graphic Rendition codes that this interpreter handles.
        """

        return [sgr for sgr in self.lookup]

    def to_code(self, value: TInterpretableValue) -> SequencerResult:
        """
        Resolves `value` into a sequence of Select Graphic Rendition attributes.
        """

        for sgr in self.lookup:
            if sgr == SelectGraphicRendition.DEFAULT.value:
                # We want to return something more specific than "everything".
                continue
            if self.lookup[sgr] == value:
                return SequencerResult(attributes=[sgr])

        return self.to_extended_attributes(value)

    def to_extended_attributes(self, value: TInterpretableValue) -> SequencerResult:
        """
        Override to provide an interpretation for Select Graphic Rendition
        attributes not present in the look-up dictionary.
        """
