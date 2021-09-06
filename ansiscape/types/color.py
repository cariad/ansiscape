from typing import Optional, TypedDict

from ansiscape.enums import ColorType, StandardColor
from ansiscape.types.rgb import RGB


class Color(TypedDict):
    color_type: ColorType
    rgb: Optional[RGB]
    standard_color: Optional[StandardColor]
