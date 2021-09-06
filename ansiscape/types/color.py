from typing import Optional, TypedDict

from ansiscape.enums import ColorType, StandardColor
from ansiscape.types.rgba import RGBA


class Color(TypedDict):
    color_type: ColorType
    rgba: Optional[RGBA]
    standard_color: Optional[StandardColor]
