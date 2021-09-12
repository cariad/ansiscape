# from typing import Dict, List, Optional, Tuple, Union, cast

# from ansiscape.enums import (
#     InterpretationKey,
#     InterpretationSpecial,
#     SelectGraphicRendition,
# )
# from ansiscape.sequence import Sequence
# from ansiscape.types import (
#     Attributes,
#     BaseSequence,
#     InterpretationDict,
#     Interpreter,
#     SequencerResult,
#     TInterpretableValue,
# )


# class DictValue(Interpreter[TInterpretableValue]):
#     def __init__(
#         self,
#         key: InterpretationKey,
#         lookup: Dict[SelectGraphicRendition, TInterpretableValue],
#     ) -> None:
#         self._key = key
#         self.lookup = lookup

#     @property
#     def key(self) -> InterpretationKey:
#         return self._key

#     @property
#     def supported_codes(self) -> List[SelectGraphicRendition]:
#         return [sgr for sgr in self.lookup]

#     def from_attributes(
#         self,
#         attrs: Attributes,
#     ) -> Tuple[TInterpretableValue, int]:
#         """Gets the interpreted value and quantity of attributes claimed."""

#         if not attrs:
#             raise ValueError("attributes list is empty")

#         try:
#             sgr = SelectGraphicRendition(attrs[0])
#         except Exception:
#             print("attrs:", attrs[0])
#             raise
#         if sgr in self.lookup:
#             return self.lookup[sgr], 0
#         return self.from_extended_attributes(attrs[1:])

#     def from_extended_attributes(
#         self,
#         attrs: Attributes,
#     ) -> Tuple[TInterpretableValue, int]:
#         """Override to implement."""
#         raise NotImplementedError()

#     def make_sequence(
#         self, value: TInterpretableValue, *parts: Union[str, BaseSequence]
#     ) -> Sequence:
#         return Sequence(
#             *parts,
#             prefix=self.make_interpretation(value),
#             suffix=self.make_interpretation(InterpretationSpecial.REVERT),
#         )

#     def make_sequence_from_attributes(
#         self,
#         attrs: Attributes,
#         *parts: Union[str, BaseSequence],
#     ) -> BaseSequence:
#         value = self.from_attributes(attrs)
#         return self.make_sequence(value[0], *parts)

#     def make_interpretation(
#         self,
#         value: Union[TInterpretableValue, InterpretationSpecial],
#     ) -> InterpretationDict:
#         return cast(InterpretationDict, {self.key.value: value})

#     def to_code(self, value: TInterpretableValue) -> SequencerResult:
#         """Resolves a value into a sequencer result."""

#         for sgr in self.lookup:
#             if sgr == SelectGraphicRendition.DEFAULT:
#                 # We want to return something more specific than "everything".
#                 continue
#             if self.lookup[sgr] == value:
#                 return SequencerResult(sgr=sgr)

#         return self.get_extended_code(value)

#     def get_extended_code(self, value: TInterpretableValue) -> SequencerResult:
#         raise NotImplementedError()

#     @property
#     def off(self) -> SelectGraphicRendition:
#         off_value = self.lookup[SelectGraphicRendition.DEFAULT]
#         print("off_value:", off_value)
#         for sgr in self.lookup:
#             if sgr == SelectGraphicRendition.DEFAULT:
#                 continue
#             if self.lookup[sgr] != off_value:
#                 continue

#             if type(self.lookup[sgr]) != type(off_value):
#                 continue

#             print("off:", sgr)
#             return sgr
#         raise ValueError("no off")

#     def sequence(self, stack: List[InterpretationDict]) -> SequencerResult:
#         """
#         Generates a sequence for the interpretation at the top of the stack. The
#         lower stack comes into play only if the top item is a reversion.
#         """
#         value = self.value(stack)
#         if value is not None:
#             return self.to_code(value)
#         return SequencerResult(sgr=self.off)

#     def reversion(
#         self,
#         stack: List[InterpretationDict],
#     ) -> Optional[TInterpretableValue]:
#         """
#         Gets the value in the lower stack that completes a reversion prescribed
#         by the top of the stack.
#         """

#         count = 0
#         while stack:
#             result = self.value(stack)
#             if result is None:
#                 # The interpretation at the top of the stack didn't concern us.
#                 continue
#             count += 1
#             # If count == 1 then we've found the value that has been
#             # reverted, but we need to find the previous value to know what
#             # we should revert _to_.
#             if count == 2:
#                 return result
#         return None

#     def value(self, stack: List[InterpretationDict]) -> Optional[TInterpretableValue]:
#         """
#         Gets the best value for this type from the interpretation at the top of
#         the stack.

#         Will return `None` if the interpretation at the top of the stack does
#         not describe this type.

#         Will hunt and return a value from the lower stack if this interpretation
#         at the top prescribes a reversion.
#         """

#         value = stack.pop().get(self.key.value, None)
#         print("value:", value)

#         if value is None:
#             # The interpretation at the top of the stack doesn't describe a
#             # change to the attribute we care about.
#             return None

#         if isinstance(value, InterpretationSpecial):
#             return self.reversion(stack)

#         return cast(TInterpretableValue, value)
