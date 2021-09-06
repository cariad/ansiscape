from ansiscape.interpreters import InterpretationDict, interpreters
from ansiscape.version import get_version


def interpret(code: str) -> InterpretationDict:
    interpretation = make_interpretation()

    if not code:
        return interpretation

    attributes = [int(attribute) for attribute in code.split(";")]

    while True:
        max_claim_this_round = 0
        min_claim_this_round = 1

        for interpreter in interpreters:
            claim = interpreter.claim(attributes)
            if claim == 0:
                continue
            max_claim_this_round = max(max_claim_this_round, claim)
            min_claim_this_round = min(min_claim_this_round, claim)
            interpreter.update(attributes[:claim], interpretation)

        if max_claim_this_round == 0:
            # None of our interpreters can handler this.
            return interpretation

        if min_claim_this_round != max_claim_this_round:
            # Many interpreters can handle the same attribute, but they must
            # all claim the same quantity off the head.
            raise Exception(f"{min_claim_this_round}, {max_claim_this_round}")

        attributes = attributes[max_claim_this_round:]
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
