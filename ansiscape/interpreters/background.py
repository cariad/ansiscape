from typing import Optional

from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.color_value import ColorValue
from ansiscape.types import Color


class BackgroundValue(ColorValue):
    def __init__(self, force: Optional[Color] = None) -> None:
        super().__init__(InterpretationKey.BACKGROUND, force)