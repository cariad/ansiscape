from typing import Union

from ansiscape.enums import MetaColor, NamedColor
from ansiscape.types.rgba import RGBA

Color = Union[MetaColor, NamedColor, RGBA]
