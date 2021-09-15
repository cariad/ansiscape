from typing import Optional, TypedDict, Union

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

# from ansiscape.types.interpretation_value import InterpretableValue

# UntypedInterpretation = Dict[str, InterpretableValue]


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


def try_merge(
    a: InterpretationDict,
    b: InterpretationDict,
) -> Optional[InterpretationDict]:
    c: InterpretationDict = {}

    for key in InterpretationKey:
        key_str = str(key.value)

        # We can't normally pluck out of a typed dictionary with random string
        # keys, but we'll ask the linter to look the other way down here for
        # performance. This function gets pummelled.
        av = a[key_str] if key_str in a else None  # type: ignore
        bv = b[key_str] if key_str in b else None  # type: ignore

        if av is None:
            if bv is None:
                # Both sides are None, so don't add the key.
                pass
            else:
                # Only B has a value, so keep B
                c[key_str] = bv  # type: ignore

        else:
            if bv is None:
                # Only A has a value, so keep B
                c[key_str] = av  # type: ignore
            else:
                # We never want to merge two values into the same dictionary
                # because then we won't be able to revert the latter. Since both
                # dictionaries have a value for this key, we can't merge them.
                return None

    return c
