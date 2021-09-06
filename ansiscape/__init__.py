from ansiscape.interpreters import InterpretationDict, interpreters
from ansiscape.version import get_version


def interpret(code: str) -> InterpretationDict:
    interpretation = make_interpretation()

    if not code:
        return interpretation

    attributes = [int(attribute) for attribute in code.split(";")]

    while True:
        count = len(attributes)

        max_claim = 0
        min_claim = 1

        for interpreter in interpreters:
            claim = interpreter.claim(attributes)
            if claim == 0:
                continue
            max_claim = max(max_claim, claim)
            min_claim = min(min_claim, claim)
            claimed = attributes[:claim]
            interpreter.update(claimed, interpretation)

        if max_claim == 0:
            # We've reached an attribute that none of our interpreters can
            # handle. Rather than skip it and risk a mess, we'll stop early.
            return interpretation

        if min_claim != max_claim:
            raise Exception(f"{min_claim}, {max_claim}")

        attributes = attributes[max_claim:]
        if not attributes:
            return interpretation

        if len(attributes) == count:
            # We've reached an attribute that none of our interpreters can
            # handle. Rather than skip it and risk a mess, we'll stop early.
            return interpretation


def make_interpretation() -> InterpretationDict:
    return InterpretationDict(
        blackletter=None,
        blink_speed=None,
        conceal=None,
        font_face=None,
        intensity=None,
        invert=None,
        italic=None,
        strike=None,
        underline=None,
        vertical_position=None,
    )


__all__ = ["get_version", "InterpretationDict"]
