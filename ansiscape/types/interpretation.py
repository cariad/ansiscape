from typing import TypedDict, Union

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
from ansiscape.types.color import Color


class Interpretation(TypedDict, total=False):
    """
    Describes an interpretation of a sequence of ANSI escape codes.

    Items cannot be `None`, but are all optional.
    """

    """
    Background colour.
    """
    background: Union[Color, InterpretationSpecial]

    """
    Blink speed.
    """
    blink: Union[Blink, InterpretationSpecial]

    """
    Calligraphy.
    """
    calligraphy: Union[Calligraphy, InterpretationSpecial]

    """
    Conceal/reveal.
    """
    conceal: Union[bool, InterpretationSpecial]

    """
    Font.
    """
    font: Union[Font, InterpretationSpecial]

    """
    Foreground colour.
    """
    foreground: Union[Color, InterpretationSpecial]

    """
    Framing.
    """
    frame: Union[Frame, InterpretationSpecial]

    """
    Ideogram.
    """
    ideogram: Union[Ideogram, InterpretationSpecial]

    """
    Weight.
    """
    weight: Union[Weight, InterpretationSpecial]

    """
    Invert colours.
    """
    invert: Union[bool, InterpretationSpecial]

    """
    Overline.
    """
    overline: Union[bool, InterpretationSpecial]

    """
    Proportional spacing.
    """
    proportional_spacing: Union[bool, InterpretationSpecial]

    """
    Strikethrough.
    """
    strike: Union[bool, InterpretationSpecial]

    """
    Underline.
    """
    underline: Union[Underline, InterpretationSpecial]
