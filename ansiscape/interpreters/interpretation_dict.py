from typing import Optional, TypedDict

from ansiscape.enums import BlinkSpeed, Intensity, Underline, VerticalPosition


class InterpretationDict(TypedDict):
    """Describes an interpretation of a sequence of ANSI escape codes."""

    """
    Describes the blinking speed of subsequent text.

    `None` should be interpreted as "no change" rather than "no blinking".
    """
    blink_speed: Optional[BlinkSpeed]

    """
    Describes the intensity of subsequent text.

    `None` should be interpreted as "no change" rather than "no intensity".
    """
    intensity: Optional[Intensity]

    """
    Describes the inversion of subsequent text.

    `None` should be interpreted as "no change" rather than "no inversion".
    """
    invert: Optional[bool]

    """
    Describes the italic of subsequent text.

    `None` should be interpreted as "no change" rather than "no italic".
    """
    italic: Optional[bool]

    """
    Describes the underline of subsequent text.

    `None` should be interpreted as "no change" rather than "no underline".
    """
    underline: Optional[Underline]

    """
    Describes the vertical position of subsequent text.

    `None` should be interpreted as "no change" rather than "no vertical
    position".
    """
    vertical_position: Optional[VerticalPosition]
