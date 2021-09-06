from typing import List

from ansiscape.interpreters import InterpretationDict, interpreters
from ansiscape.version import get_version


def make_attributes(code: str) -> List[int]:
    code = code.strip()
    if not code:
        return []
    return [int(attribute) for attribute in code.split(";")]


def interpret(code: str) -> InterpretationDict:
    interpretation = make_interpretation()
    remaining_attributes = make_attributes(code)

    while True:
        if not remaining_attributes:
            return interpretation

        this_round_claimed = 0

        for interpreter in interpreters:
            claim = interpreter.update(remaining_attributes, interpretation)
            if not claim:
                continue

            this_round_claimed = this_round_claimed or claim

            if claim != this_round_claimed:
                # Many interpreters can handle the same attribute, but they
                # must all claim the same quantity off the head.
                raise Exception(f"{claim}, {this_round_claimed}")

        if not this_round_claimed:
            # None of our interpreters can handle the attribute at the start of
            # the list. Rather than skip it and risk a mess, we'll stop now.
            return interpretation

        remaining_attributes = remaining_attributes[this_round_claimed:]


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
