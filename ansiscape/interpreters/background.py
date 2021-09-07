from typing import Optional

from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.color_value import ColorValue
from ansiscape.types import Color2


class BackgroundValue(ColorValue):
    def __init__(self, force: Optional[Color2] = None) -> None:
        super().__init__(InterpretationKey.BACKGROUND, force)
