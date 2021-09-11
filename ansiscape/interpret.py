from typing import Any, Dict

from ansiscape.enums import SelectGraphicRendition
from ansiscape.interpreters import interpretations
from ansiscape.types import Attributes


def make_attributes(sequence: str) -> Attributes:
    """
    Splits a sequence into a list of attributes.

    For example, splits `"38;2;0;0;0"` into `[38, 2, 0, 0, 0]`.
    """

    code = sequence.strip()
    if not code:
        return []
    return [int(attribute) for attribute in code.split(";")]


def interpret_as_any(sequence: str) -> Dict[str, Any]:
    """
    Interprets a sequence into a descriptive dictionary.

    For example, interprets `"38;2;0;0;0"` into `{"foreground": (0, 0, 0, 1)}`.
    """

    remaining_attributes = make_attributes(sequence)

    wip: Dict[str, Any] = {}

    while True:
        if not remaining_attributes:
            return wip

        this_round_claimed = 0

        head_code = SelectGraphicRendition(remaining_attributes[0])
        handlers = interpretations[head_code]

        if not handlers:
            return wip

        for handler in handlers:
            value, claim = handler.value(remaining_attributes[1:])
            wip[handler.key.value] = value
            claim += 1  # Include the header that we didn't pass down
            this_round_claimed = this_round_claimed or claim
            if claim != this_round_claimed:
                # Many interpreters can handle the same attribute, but they
                # must all claim the same quantity off the head.
                raise Exception(f"{claim}, {this_round_claimed}")

        remaining_attributes = remaining_attributes[this_round_claimed:]

        if not remaining_attributes:
            return wip
