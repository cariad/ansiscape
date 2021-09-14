from typing import Any, Dict, TypedDict, Union, cast

from ansiscape.enums import (
    Blink,
    Calligraphy,
    Font,
    Frame,
    Ideogram,
    InterpretationSpecial,
    Underline,
    Weight,
)
from ansiscape.enums.interpretation_key import InterpretationKey
from ansiscape.types.color import Color


class InterpretationDict(TypedDict, total=False):
    """Describes an interpretation of a sequence of ANSI escape codes."""

    """
    Describes the background colour of subsequent text.

    `None` should be interpreted as "no change" rather than "no background
    colour".
    """
    background: Union[Color, InterpretationSpecial]

    """
    Describes the blinking speed of subsequent text.

    `None` should be interpreted as "no change" rather than "no blinking".
    """
    blink: Union[Blink, InterpretationSpecial]

    """
    Describes the calligraphy of subsequent text.

    `None` should be interpreted as "no change" rather than "no calligraphy".
    """
    calligraphy: Union[Calligraphy, InterpretationSpecial]

    """
    Describes the concealing of subsequent text.

    `None` should be interpreted as "no change" rather than "no concealing".
    """
    conceal: Union[bool, InterpretationSpecial]

    """
    Describes the font face of subsequent text.

    `None` should be interpreted as "no change" rather than "no font face".
    """
    font: Union[Font, InterpretationSpecial]

    """
    Describes the foreground colour of subsequent text.

    `None` should be interpreted as "no change" rather than "no foreground
    colour".
    """
    foreground: Union[Color, InterpretationSpecial]

    """
    Describes the framing of subsequent text.

    `None` should be interpreted as "no change" rather than "no framing".
    """
    frame: Union[Frame, InterpretationSpecial]

    """
    Describes the ideogram formatting of subsequent text.

    `None` should be interpreted as "no change" rather than "no ideogram".
    """
    ideogram: Union[Ideogram, InterpretationSpecial]

    """
    Describes the intensity of subsequent text.

    `None` should be interpreted as "no change" rather than "no intensity".
    """
    weight: Union[Weight, InterpretationSpecial]

    """
    Describes the inversion of subsequent text.

    `None` should be interpreted as "no change" rather than "no inversion".
    """
    invert: Union[bool, InterpretationSpecial]

    """
    Describes the overline of subsequent text.

    `None` should be interpreted as "no change" rather than "no overline".
    """
    overline: Union[bool, InterpretationSpecial]

    """
    Describes the proportional spacing of subsequent text.

    `None` should be interpreted as "no change" rather than "no proportional
    spacing".
    """
    proportional_spacing: Union[bool, InterpretationSpecial]

    """
    Describes the strikethrough of subsequent text.

    `None` should be interpreted as "no change" rather than "no strikethrough".
    """
    strike: Union[bool, InterpretationSpecial]

    """
    Describes the underline of subsequent text.

    `None` should be interpreted as "no change" rather than "no underline".
    """
    underline: Union[Underline, InterpretationSpecial]


def merge_interpretation(
    a: InterpretationDict, b: InterpretationDict
) -> InterpretationDict:
    c: Dict[str, Any] = {}
    # any_a = cast(Dict[str, Any], a)
    # any_b = cast(Dict[str, Any], b)

    for key in InterpretationKey:
        av = a.get(key.value, None)
        bv = b.get(key.value, None)

        if av is None and bv is None:
            continue

        # if av is InterpretationSpecial and bv is not None and bv is not InterpretationSpecial:
        #     c[key.value] = bv
        #     continue

        if bv is not None:
            c[key.value] = bv
            continue

    return cast(InterpretationDict, c)
