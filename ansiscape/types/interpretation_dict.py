from typing import Optional, TypedDict

from ansiscape.enums import (
    BlinkSpeed,
    FontFace,
    Frame,
    Ideogram,
    Intensity,
    Underline,
    VerticalPosition,
)
from ansiscape.types.color import Color


class InterpretationDict(TypedDict):
    """Describes an interpretation of a sequence of ANSI escape codes."""

    """
    Describes the blackletter of subsequent text.

    `None` should be interpreted as "no change" rather than "no blackletter".
    """
    blackletter: Optional[bool]

    """
    Describes the blinking speed of subsequent text.

    `None` should be interpreted as "no change" rather than "no blinking".
    """
    blink_speed: Optional[BlinkSpeed]

    """
    Describes the concealing of subsequent text.

    `None` should be interpreted as "no change" rather than "no concealing".
    """
    conceal: Optional[bool]

    """
    Describes the font face of subsequent text.

    `None` should be interpreted as "no change" rather than "no font face".
    """
    font_face: Optional[FontFace]

    """
    Describes the foreground colour of subsequent text.

    `None` should be interpreted as "no change" rather than "no foreground
    colour".
    """
    foreground_color: Optional[Color]

    """
    Describes the framing of subsequent text.

    `None` should be interpreted as "no change" rather than "no framing".
    """
    frame: Optional[Frame]

    """
    Describes the ideogram formatting of subsequent text.

    `None` should be interpreted as "no change" rather than "no ideogram".
    """
    ideogram: Optional[Ideogram]

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
    Describes the overline of subsequent text.

    `None` should be interpreted as "no change" rather than "no overline".
    """
    overline: Optional[bool]

    """
    Describes the proportional spacing of subsequent text.

    `None` should be interpreted as "no change" rather than "no proportional
    spacing".
    """
    proportional_spacing: Optional[bool]

    """
    Describes the strikethrough of subsequent text.

    `None` should be interpreted as "no change" rather than "no strikethrough".
    """
    strike: Optional[bool]

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