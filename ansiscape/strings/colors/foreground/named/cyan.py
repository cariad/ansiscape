from ansiscape.enums import StandardColor
from ansiscape.strings.colors.foreground.foreground import Foreground
from ansiscape.types import Color


class Cyan(Foreground):
    @property
    def color(self) -> Color:
        return StandardColor.CYAN
