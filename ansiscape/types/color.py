from typing import Union

from ansiscape.enums import ColorSpecial, StandardColor
from ansiscape.types.rgba import RGBA

Color = Union[ColorSpecial, RGBA, StandardColor]
