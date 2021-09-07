from typing import Literal, Union

from ansiscape.enums import StandardColor
from ansiscape.types.rgba import RGBA

Color = Union[StandardColor, RGBA, Literal[False]]
