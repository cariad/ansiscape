from ansiscape.interpreters import InterpretationDict, interpreters
from ansiscape.version import get_version


def interpret(code: str) -> InterpretationDict:
    interpretation = make_interpretation()

    if not code:
        return interpretation

    attributes = [int(attribute) for attribute in code.split(";")]

    while True:
        count = len(attributes)

        if attributes[0] == 0:
            # Make sure everyone gets this reset!
            for interpreter in interpreters:
                if interpreter.claim(attributes) == 1:
                    interpreter.update(attributes, interpretation)
            attributes = attributes[1:]
            if not attributes:
                return interpretation

        for interpreter in interpreters:
            claim = interpreter.claim(attributes)
            if not claim:
                continue
            claimed = attributes[:claim]
            interpreter.update(claimed, interpretation)
            attributes = attributes[claim:]
            if not attributes:
                return interpretation

        if len(attributes) == count:
            # We've reached an attribute that none of our interpreters can
            # handle. Rather than skip it and risk a mess, we'll stop early.
            return interpretation


def make_interpretation() -> InterpretationDict:
    return InterpretationDict(
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
