from typing import Any, List, Optional, Tuple, Union

from ansiscape.enums import InterpretationKey
from ansiscape.handlers import get_interpreter
from ansiscape.types import (
    Attributes,
    InterpretationDict,
    SequencePart,
    SequenceProtocol,
    try_merge,
)


class Sequence(SequenceProtocol):
    def __init__(
        self,
        *parts: SequencePart,
        prefix: Optional[InterpretationDict] = None,
        suffix: Optional[InterpretationDict] = None,
    ) -> None:

        # `self._parts` will never contain a Sequence; only that Sequence's
        # strings and interpretations.
        self._parts: List[Union[str, InterpretationDict]] = []
        self.extend([prefix, *parts, suffix])


    def __add__(self, other: Any) -> "SequenceProtocol":
        copy = Sequence(*self.parts)

        if isinstance(other, str):
            copy.append(other)
        else:
            copy.extend_sequence(other.parts)

        return copy

    def extend(self, parts: List[Union[SequencePart, None]]) -> None:
        for part in parts:
            if part is None:
                continue
            self.append(part)


    def extend_sequence(self, parts: List[Union[str, InterpretationDict]]) -> None:
        for part in parts:
            self.append(part)




    def append(self, part: SequencePart) -> None:
        prev = self._parts[-1] if self._parts else None

        # print("appending:", prev, part)

        # If the part we're about to append and the previously-added part
        # are both dictionaries then try to merge them:
        if isinstance(part, dict):
            if isinstance(prev, dict):
                join = try_merge(prev, part)
                if join is None:
                    # If the join fails then just include the part as-is:
                    self._parts.append(part)
                else:
                    # If the join succeeds then replace the previous part and
                    # skip the current one:
                    # print("joined: ", prev, part, join)
                    self._parts[-1] = join

            elif part:
                self._parts.append(part)

        elif isinstance(part, Sequence):
            self.extend_sequence(part.parts)

        elif isinstance(part, str):
            if isinstance(prev, str):
                self._parts[-1] = prev + part
            elif part:
                self._parts.append(part)

        else:
            NotImplementedError(f"unhandled part type: {type(part)} ({part})")

    @property
    def parts(self) -> List[Union[str, InterpretationDict]]:
        """
        Gets all the child strings and interpretations. Intentionally does not
        get child sequences, but their strings and interpretations instead.
        """
        return self._parts



    # @property
    # def args(self) -> List[SequencePart]:
    #     args: List[SequencePart] = []

    #     for part in self.parts:
    #         if isinstance(part, str) or isinstance(part, dict):
    #             args.append(part)
    #         else:
    #             args.extend(part.args)

    #     return args

    def __str__(self) -> str:
        return self.encode()

    # @property
    # def children(self) -> Iterator[Union[str, InterpretationDict]]:
    #     """
    #     Yields all the child strings and interpretations. Intentionally does not
    #     yield child sequences, but their strings and interpretations instead.
    #     """

    #     for arg in self.args:
    #         if isinstance(arg, str):
    #             yield arg

    #         elif isinstance(arg, dict):
    #             yield arg

    #         elif arg:
    #             for child in arg.children:
    #                 if child:
    #                     yield child

    def encode(self) -> str:
        """
        Encodes the sequence into a single string with embedded escape codes.
        """

        wip = ""
        stack: List[InterpretationDict] = []
        for part in self.parts:
            if isinstance(part, str):
                wip += part

            else:
                stack.append(part)
                wip += self.encode_escape_sequence(stack)
                continue

        return wip

    def encode_escape_sequence(self, stack: List[InterpretationDict]) -> str:
        """
        Encodes the interpretation at the top of the stack into an embeddable escape
        code.

        The lower stack will be read only if the interpration at the top prescribes
        a reversion.
        """

        sequences: List[Attributes] = [[]]
        interpretation = stack[-1]

        for key in InterpretationKey:
            if interpretation.get(key.value, None) is None:
                continue

            # Intentionally send a copy of the stack because inner reversion
            # resolution will pop:
            result = get_interpreter(key).sequence([*stack])

            sequence = [result["sgr"].value]
            if additional := result.get("additional", None):
                sequence.extend(additional)

            if result.get("must_isolate", False):
                sequences.append(sequence)
            else:
                sequences[0].extend(sequence)
        code = "".join([f"\033[{';'.join([str(a) for a in s])}m" for s in sequences])
        return code
