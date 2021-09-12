from typing import Any, Dict

from ansiscape.enums import SelectGraphicRendition
from ansiscape.handlers import get_interpreters_for_sgr

# from ansiscape.interpreters import interpretations
from ansiscape.types import Attributes
from ansiscape.types.interpretation_dict import InterpretationDict


def make_attributes(sequence: str) -> Attributes:
    """
    Splits a sequence into a list of attributes.

    For example, splits `"38;2;0;0;0"` into `[38, 2, 0, 0, 0]`.
    """

    code = sequence.strip()
    if not code:
        return []
    return [int(attribute) for attribute in code.split(";")]


def interpret(sequence: str) -> InterpretationDict:
    d = interpret_as_any(sequence)
    i: InterpretationDict = {}

    if background := d.get("background", None):
        i["background"] = background

    if blink := d.get("blink", None):
        i["blink"] = blink

    if calligraphy := d.get("calligraphy", None):
        i["calligraphy"] = calligraphy

    if conceal := d.get("conceal", None):
        i["conceal"] = conceal

    if font := d.get("font", None):
        i["font"] = font

    if foreground := d.get("foreground", None):
        i["foreground"] = foreground

    if frame := d.get("frame", None):
        i["frame"] = frame

    if ideogram := d.get("ideogram", None):
        i["ideogram"] = ideogram

    if weight := d.get("weight", None):
        i["weight"] = weight

    if invert := d.get("invert", None):
        i["invert"] = invert
    if overline := d.get("overline", None):
        i["overline"] = overline

    if proportional_spacing := d.get("proportional_spacing", None):
        i["proportional_spacing"] = proportional_spacing
    if strike := d.get("strike", None):
        i["strike"] = strike
    if underline := d.get("underline", None):
        i["underline"] = underline

    return i


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

        sgr = SelectGraphicRendition(remaining_attributes[0])
        interpreters = get_interpreters_for_sgr(sgr)
        # handlers = interpretations[sgr]

        # if not handlers:
        #     return wip

        for interpreter in interpreters:
            value, claim = interpreter.from_attributes(remaining_attributes)
            wip[interpreter.key.value] = value
            claim += 1  # Include the header that we didn't pass down
            this_round_claimed = this_round_claimed or claim
            if claim != this_round_claimed:
                # Many interpreters can handle the same attribute, but they
                # must all claim the same quantity off the head.
                raise Exception(f"{claim}, {this_round_claimed}")

        remaining_attributes = remaining_attributes[this_round_claimed:]

        if not remaining_attributes:
            return wip
