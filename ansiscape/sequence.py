from typing import Iterator, List, Union, cast

from ansiscape.enums import InterpretationKey
from ansiscape.enums.interpretation_special import InterpretationSpecial
from ansiscape.handlers import get_interpreter
from ansiscape.types import (
    Attributes,
    InterpretationDict,
    SequencePart,
    SequenceProtocol,
    try_merge,
)
from ansiscape.types.interpretation_dict import UntypedInterpretation


class Sequence(SequenceProtocol):
    def __init__(self, *parts: SequencePart) -> None:
        self.__parts = parts

    def extend(self, *parts: SequencePart) -> SequenceProtocol:
        self.__parts = (*self.__parts, *parts)
        return self

    @property
    def flatten(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Gets a flat (but not reduced) list of all parts and children's parts.
        """

        index = 0
        count = len(self.__parts)
        while index < count:
            part = self.__parts[index]
            if isinstance(part, SequenceProtocol):
                for sub in part.parts:
                    yield sub
            else:
                yield part
            index += 1

    @property
    def parts(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Gets all the child strings and interpretations. Intentionally does not
        get child sequences, but their strings and interpretations instead.
        """

        str_wip = ""
        dict_wip: UntypedInterpretation = {}

        for part in self.flatten:

            if isinstance(part, str):
                if len(dict_wip) > 0:
                    yield dict_wip  # type: ignore
                    dict_wip = {}
                str_wip += part

            else:
                if len(str_wip) > 0:
                    yield str_wip
                    str_wip = ""

                merged = try_merge(dict_wip, part)  # type: ignore

                if merged is None:
                    yield dict_wip  # type: ignore
                    dict_wip = part  # type: ignore
                else:
                    dict_wip = merged

        if dict_wip:
            yield cast(InterpretationDict, dict_wip)
        if str_wip:
            yield str_wip

    def __str__(self) -> str:
        print("encoding...")
        return self.encode()

    def encode(self) -> str:
        """
        Encodes the sequence into a single string with embedded escape codes.
        """

        wip = ""
        stack: List[UntypedInterpretation] = []
        for part in self.parts:
            if isinstance(part, str):
                wip += part

            else:
                # `part` is a typed dictionary, but we intentionally ignore
                # typing for performance down here.
                stack.append(part)  # type: ignore
                wip += self.encode_escape_sequence(stack=stack, index=len(stack) - 1)
                continue

        return wip

    def encode_escape_sequence(
        self,
        stack: List[UntypedInterpretation],
        index: int,
    ) -> str:
        """
        Encodes the interpretation at the top of the stack into an embeddable escape
        code.

        The lower stack will be read only if the interpration at the top prescribes
        a reversion.
        """

        sequences: List[Attributes] = [[]]
        interpretation = stack[index]

        for key in InterpretationKey:
            key_str = str(key.value)

            if key_str not in interpretation:
                continue

            value = interpretation[key_str]

            if value is None:
                continue

            interpreter = get_interpreter(key_str)

            if not isinstance(value, InterpretationSpecial):
                result = interpreter.to_code(value)
            else:
                result = interpreter.find_reversion(stack=stack, index=index)

            sequence = [result["sgr"].value]
            if additional := result.get("additional", None):
                sequence.extend(additional)

            if result.get("must_isolate", False):
                sequences.append(sequence)
            else:
                sequences[0].extend(sequence)
        code = "".join([f"\033[{';'.join([str(a) for a in s])}m" for s in sequences])
        return code
