from ansiscape.enums import StandardColor
from ansiscape.strings.colors.foreground.foreground import Foreground
from ansiscape.types import Color


class White(Foreground):
    @property
    def color(self) -> Color:
        return StandardColor.WHITE
