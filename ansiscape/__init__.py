from typing import Optional

from ansiscape.interpreters import InterpretationDict, interpreters
from ansiscape.version import get_version


def interpret(code: str) -> InterpretationDict:
    interpretation = make_interpretation()

    if not code:
        return interpretation

    attributes = [int(attribute) for attribute in code.split(";")]

    while True:
        max_claim = 0
        min_claim: Optional[int] = None

        for interpreter in interpreters:
            claim = interpreter.claim(attributes)
            if claim == 0:
                continue
            max_claim = max(max_claim, claim)
            min_claim = claim if min_claim is None else min(min_claim, claim)
            interpreter.update(attributes[:claim], interpretation)

        if max_claim == 0:
            # None of our interpreters can handler this.
            return interpretation

        if min_claim != max_claim:
            # Many interpreters can handle the same attribute, but they must
            # all claim the same quantity off the head.
            raise Exception(f"{min_claim}, {max_claim}")

        attributes = attributes[max_claim:]
        if not attributes:
            # Successfully interpreted the entire chain.
            return interpretation


def make_interpretation() -> InterpretationDict:
    return InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        foreground_color=None,
        frame=None,
        ideogram=None,
        intensity=None,
        invert=None,
        italic=None,
        overline=None,
        proportional_spacing=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )


__all__ = ["get_version", "InterpretationDict"]
