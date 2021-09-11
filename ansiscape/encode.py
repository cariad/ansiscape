from typing import List, Union

from ansiscape.encoders import get_encoder
from ansiscape.enums import InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.types import Attributes, InterpretationDict


def encode(*parts: Union[str, InterpretationDict]) -> str:
    """
    Encodes a series of strings and formatting interpretations into a single
    string with embedded escape codes.
    """

    wip = ""
    history: List[InterpretationDict] = []
    for arg in parts:

        if isinstance(arg, dict) and not arg:
            # Don't add empty dictionaries.
            continue

        if isinstance(arg, str):
            wip += arg
        else:
            wip += sequence(interpretation=arg, history=history)
            history.append(arg)

    return wip


def sequence(
    interpretation: InterpretationDict,
    history: List[InterpretationDict],
) -> str:
    sequences: List[Attributes] = [[]]

    for key in interpretation:
        if interpretation.get(key, None) is None:
            continue

        interpretation_key = InterpretationKey(key)
        sequencer = get_encoder(interpretation_key)
        stack = [*history, interpretation]
        result = sequencer.sequence(stack)

        sgr = result.get("sgr", SelectGraphicRendition.DEFAULT)
        additional = result.get("additional", None) or []

        seq: List[int] = [sgr.value, *additional]

        if result.get("must_isolate", False):
            sequences.append(seq)
        else:
            sequences[0].extend(seq)

    return "".join([sequence_attributes(attrs) for attrs in sequences])


def sequence_attributes(attrs: Attributes) -> str:
    return f"\033[{';'.join([str(attr) for attr in attrs])}m"
