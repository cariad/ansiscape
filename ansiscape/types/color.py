from typing import Union

from ansiscape.enums import ColorSpecial, NamedColor
from ansiscape.types.rgba import RGBA

Color = Union[ColorSpecial, RGBA, NamedColor]
