from typing import TypedDict, Union

from ansiscape.enums import (
    Blink,
    Calligraphy,
    Font,
    Frame,
    Ideogram,
    MetaInterpretation,
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
    background: Union[Color, MetaInterpretation]

    """
    Blink speed.
    """
    blink: Union[Blink, MetaInterpretation]

    """
    Calligraphy.
    """
    calligraphy: Union[Calligraphy, MetaInterpretation]

    """
    Conceal/reveal.
    """
    conceal: Union[bool, MetaInterpretation]

    """
    Font.
    """
    font: Union[Font, MetaInterpretation]

    """
    Foreground colour.
    """
    foreground: Union[Color, MetaInterpretation]

    """
    Framing.
    """
    frame: Union[Frame, MetaInterpretation]

    """
    Ideogram.
    """
    ideogram: Union[Ideogram, MetaInterpretation]

    """
    Invert colours.
    """
    invert: Union[bool, MetaInterpretation]

    """
    Overline.
    """
    overline: Union[bool, MetaInterpretation]

    """
    Proportional spacing.
    """
    proportional_spacing: Union[bool, MetaInterpretation]

    """
    Strikethrough.
    """
    strike: Union[bool, MetaInterpretation]

    """
    Underline.
    """
    underline: Union[Underline, MetaInterpretation]

    """
    Weight.
    """
    weight: Union[Weight, MetaInterpretation]
