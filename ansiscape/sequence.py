from typing import Iterator, List, Tuple, Union

from ansiscape.enums import InterpretationKey
from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.handlers import get_interpreter
from ansiscape.types import (
    Attributes,
    InterpretationDict,
    SequencePart,
    SequenceType,
    try_merge,
)


class Sequence(SequenceType):
    """A sequence of strings, formatting interpretations and sub-sequences."""

    def __init__(self, *parts: SequencePart) -> None:
        self._parts = parts

    def __str__(self) -> str:
        return self.encoded

    @staticmethod
    def encode_escape_sequence(stack: List[InterpretationDict], index: int) -> str:
        """
        Encodes the interpretation at `index` of `stack`.

        The lower stack will be read only if the interpration at `index`
        prescribes a reversion.
        """

        sequences: List[Attributes] = [[]]
        interpretation = stack[index]

        for key in InterpretationKey:
            key_str = str(key.value)

            if key_str not in interpretation:
                continue

            # We can't normally pluck out of a typed dictionary with random
            # string keys, but we'll ask the linter to look the other way down
            # here for performance. This function gets pummelled.
            value = interpretation[key_str]  # type: ignore

            interpreter = get_interpreter(key_str)

            if not isinstance(value, InterpretationSpecial):
                result = interpreter.to_code(value)
            else:
                result = interpreter.find_reversion(stack=stack, index=index)

            if result.get("must_isolate", False):
                sequences.append(result["attributes"])
            else:
                sequences[0].extend(result["attributes"])

        code = "".join([f"\033[{';'.join([str(a) for a in s])}m" for s in sequences])
        return code

    @property
    def encoded(self) -> str:
        """
        Encodes the sequence into a single string with embedded escape codes.
        """

        wip = ""
        stack: List[InterpretationDict] = []
        for part in self.resolved:
            if isinstance(part, str):
                wip += part
            else:
                stack.append(part)
                index = len(stack) - 1
                wip += self.encode_escape_sequence(stack=stack, index=index)

        return wip

    def extend(self, *parts: SequencePart) -> None:
        """Extends this sequence."""
        self._parts = (*self._parts, *parts)

    @property
    def flatten(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Gets a flat (but not reduced) list of this sequence's and child
        sequence's parts.
        """

        index = 0
        count = len(self._parts)
        while index < count:
            part = self._parts[index]
            if isinstance(part, SequenceType):
                for sub in part.resolved:
                    yield sub
            else:
                yield part
            index += 1

    @property
    def parts(self) -> Tuple[SequencePart, ...]:
        """
        Gets the internal parts of this sequence. You probably want to use
        `resolved` instead.
        """

        return self._parts

    @property
    def resolved(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Flattens child sequences and gets all strings and interpretations.
        """

        str_wip = ""
        dict_wip: InterpretationDict = {}

        for part in self.flatten:

            if isinstance(part, str):
                if len(dict_wip) > 0:
                    yield dict_wip
                    dict_wip = {}
                str_wip += part

            else:
                if len(str_wip) > 0:
                    yield str_wip
                    str_wip = ""

                merged = try_merge(dict_wip, part)

                if merged is None:
                    yield dict_wip
                    dict_wip = part
                else:
                    dict_wip = merged

        if dict_wip:
            yield dict_wip

        if str_wip:
            yield str_wip
