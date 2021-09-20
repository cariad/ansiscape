from json import dumps
from re import finditer
from typing import Iterator, List, Optional, TextIO, Union

from ansiscape.enums import InterpretationKey, MetaInterpretation
from ansiscape.handlers import get_interpreter, get_interpreter_for_sgr_int
from ansiscape.types import Attributes, Interpretation, SequencePart, SequenceType


class Sequence(SequenceType):
    """A sequence of strings, formatting interpretations and sub-sequences."""

    def __init__(self, *parts: SequencePart) -> None:
        self._parts: List[SequencePart] = []

        for part in parts:
            if not isinstance(part, str):
                self._parts.append(part)
                continue

            interpretation = Interpretation()
            prev_match_end = 0

            for m in finditer("\033\\[([0-9;]+)m", part):
                if m.start() > prev_match_end:
                    if interpretation:
                        self._parts.append(interpretation)
                        interpretation = Interpretation()
                    self._parts.append(part[prev_match_end : m.start()])

                attrs = [int(a) for a in m.group(1).split(";")]

                while len(attrs) > 0:
                    interpreter = get_interpreter_for_sgr_int(attrs[0])
                    claimed = interpreter.interpret(
                        attrs=attrs,
                        interpretation=interpretation,
                    )
                    attrs = attrs[claimed:]

                prev_match_end = m.end()

            if interpretation:
                self._parts.append(interpretation)

            if prev_match_end < len(part):
                self._parts.append(part[prev_match_end:])

    def __str__(self) -> str:
        return self.encoded

    @staticmethod
    def encode_escape_sequence(stack: List[Interpretation], index: int) -> str:
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

            if not isinstance(value, MetaInterpretation):
                result = interpreter.to_code(value)
            else:
                result = interpreter.find_reversion(stack=stack, index=index)

            if result.get("must_isolate", False):
                sequences.append(result["attributes"])
            else:
                sequences[0].extend(result["attributes"])

        codes = ""

        for sequence in sequences:
            if not sequence:
                continue
            codes += f"\033[{';'.join([str(attr) for attr in sequence])}m"

        return codes

    @property
    def encoded(self) -> str:
        """
        Encodes the sequence into a single string with embedded escape codes.
        """

        wip = ""
        stack: List[Interpretation] = []
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
        self._parts.extend(parts)

    @property
    def flatten(self) -> Iterator[Union[str, Interpretation]]:
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
    def parts(self) -> List[SequencePart]:
        """
        Gets the internal parts of this sequence. You probably want to use
        `resolved` instead.
        """

        return self._parts

    @property
    def resolved(self) -> Iterator[Union[str, Interpretation]]:
        """
        Flattens child sequences and gets all strings and interpretations.
        """

        str_wip = ""
        dict_wip: Interpretation = {}

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

                merged = self.try_merge(dict_wip, part)

                if merged is None:
                    yield dict_wip
                    dict_wip = part
                else:
                    dict_wip = merged

        if dict_wip:
            yield dict_wip

        if str_wip:
            yield str_wip

    @staticmethod
    def try_merge(
        a: Interpretation,
        b: Interpretation,
    ) -> Optional[Interpretation]:
        c: Interpretation = {}

        for key in InterpretationKey:
            key_str = str(key.value)

            # We can't normally pluck out of a typed dictionary with random string
            # keys, but we'll ask the linter to look the other way down here for
            # performance. This function gets pummelled.
            av = a[key_str] if key_str in a else None  # type: ignore
            bv = b[key_str] if key_str in b else None  # type: ignore

            if av is None:
                if bv is None:
                    # Both sides are None, so don't add the key.
                    pass
                else:
                    # Only B has a value, so keep B
                    c[key_str] = bv  # type: ignore

            else:
                if bv is None:
                    # Only A has a value, so keep B
                    c[key_str] = av  # type: ignore
                else:
                    # We never want to merge two values into the same dictionary
                    # because then we won't be able to revert the latter. Since both
                    # dictionaries have a value for this key, we can't merge them.
                    return None

        return c

    def write_json(self, writeable: TextIO) -> None:
        """Writes this sequence to a JSON string."""

        writeable.write("[")
        is_first = True
        for r in self.resolved:
            if is_first:
                is_first = False
            else:
                writeable.write(",")
            writeable.write(dumps(r, sort_keys=True))
        writeable.write("]\n")
