from typing import Any, Iterator, List, Optional, Tuple, Union

from ansiscape.enums import InterpretationKey
from ansiscape.handlers import get_interpreter
from ansiscape.types import (
    Attributes,
    InterpretationDict,
    SequencePart,
    SequenceProtocol,
)


class Sequence(SequenceProtocol):
    def __init__(
        self,
        *parts: SequencePart,
        prefix: Optional[InterpretationDict] = None,
        suffix: Optional[InterpretationDict] = None,
    ) -> None:
        self.parts = parts
        if prefix is not None:
            self.parts = (prefix, *self.parts)
        if suffix is not None:
            self.parts = (*self.parts, suffix)

    def __add__(self, other: Any) -> "SequenceProtocol":
        if isinstance(other, str):
            return Sequence(*(*self.parts, other))

        parts: Tuple[SequencePart, ...] = ()

        # if isinstance(other, Sequence):
        #     join=merge_interpretation(self.suffix, other.prefix)
        #     parts = (*self.parts, join, *other.parts)

        if not parts:
            parts = (*self.parts, *other.parts)

        return Sequence(*parts)

    @property
    def args(self) -> List[SequencePart]:
        args: List[SequencePart] = []

        for part in self.parts:
            if isinstance(part, str) or isinstance(part, dict):
                args.append(part)
            else:
                args.extend(part.args)

        return args

    def __str__(self) -> str:
        return self.encode()

    @property
    def children(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Yields all the child strings and interpretations. Intentionally does not
        yield child sequences, but their strings and interpretations instead.
        """

        for arg in self.args:
            if isinstance(arg, str):
                yield arg

            elif isinstance(arg, dict):
                yield arg

            elif arg:
                for child in arg.children:
                    if child:
                        yield child

    def encode(self) -> str:
        """
        Encodes the sequence into a single string with embedded escape codes.
        """

        wip = ""
        stack: List[InterpretationDict] = []
        for child in self.children:
            if isinstance(child, str):
                wip += child

            else:
                if not child:
                    # Don't add empty dictionaries.
                    continue
                stack.append(child)
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
