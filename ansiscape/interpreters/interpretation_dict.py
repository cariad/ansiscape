from typing import Optional, TypedDict

from ansiscape.enums import Intensity, VerticalPosition


class InterpretationDict(TypedDict):
    """Describes an interpretation of a sequence of ANSI escape codes."""

    """
    Describes the intensity of subsequent text.

    `None` should be interpreted as "no change" rather than "no intensity".
    """
    intensity: Optional[Intensity]

    """
    Describes the italic of subsequent text.

    `None` should be interpreted as "no change" rather than "no italic".
    """
    italic: Optional[bool]

    """
    Describes the vertical position of subsequent text.

    `None` should be interpreted as "no change" rather than "no vertical
    position".
    """
    vertical_position: Optional[VerticalPosition]
