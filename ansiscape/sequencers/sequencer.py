from abc import ABC, abstractclassmethod, abstractproperty
from typing import Generic, List, Optional, TypeVar, cast

from ansiscape.enums import InterpretationKey, InterpretationSpecial
from ansiscape.types import InterpretationDict, SequencerResult

TValue = TypeVar("TValue")


class Sequencer(ABC, Generic[TValue]):
    @abstractproperty
    def key(self) -> InterpretationKey:
        ...

    def sequence(self, stack: List[InterpretationDict]) -> SequencerResult:
        """
        Generates a sequence for the interpretation at the top of the stack. The
        lower stack comes into play only if the top item is a reversion.
        """
        return self.resolve(self.value(stack))

    def reversion(self, stack: List[InterpretationDict]) -> Optional[TValue]:
        """
        Gets the value in the lower stack that completes a reversion prescribed
        by the top of the stack.
        """

        count = 0
        while stack:
            result = self.value(stack)
            if result is None:
                # The interpretation at the top of the stack didn't concern us.
                continue
            count += 1
            # If count == 1 then we've found the value that has been
            # reverted, but we need to find the previous value to know what
            # we should revert _to_.
            if count == 2:
                return result
        return None

    @abstractclassmethod
    def resolve(cls, value: Optional[TValue]) -> SequencerResult:
        """Resolves a value into a sequencer result."""

    def value(self, stack: List[InterpretationDict]) -> Optional[TValue]:
        """
        Gets the best value for this type from the interpretation at the top of
        the stack.

        Will return `None` if the interpretation at the top of the stack does
        not describe this type.

        Will hunt and return a value from the lower stack if this interpretation
        at the top prescribes a reversion.
        """

        value = stack.pop().get(self.key.value, None)

        if value is None:
            # The interpretation at the top of the stack doesn't describe a
            # change to the attribute we care about.
            return None

        if isinstance(value, InterpretationSpecial):
            if value == InterpretationSpecial.REVERT:
                return self.reversion(stack)
            raise ValueError()

        return cast(TValue, value)
