from typing import List, Union

from ansiscape.encoders import get_encoder
from ansiscape.enums import InterpretationKey
from ansiscape.types import Attributes, InterpretationDict


def encode(*parts: Union[str, InterpretationDict]) -> str:
    """
    Encodes a series of strings and formatting interpretations into a single
    string with embedded escape codes.
    """

    wip = ""
    stack: List[InterpretationDict] = []
    for arg in parts:
        if isinstance(arg, str):
            wip += arg
            continue

        if not arg:
            # Don't add empty dictionaries.
            continue

        stack.append(arg)
        wip += encode_escape_sequence(stack)

    return wip


def encode_escape_sequence(stack: List[InterpretationDict]) -> str:
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
        result = get_encoder(key).sequence([*stack])

        sequence = [result["sgr"].value]
        if additional := result.get("additional", None):
            sequence.extend(additional)

        if result.get("must_isolate", False):
            sequences.append(sequence)
        else:
            sequences[0].extend(sequence)

    return "".join([f"\033[{';'.join([str(a) for a in s])}m" for s in sequences])
