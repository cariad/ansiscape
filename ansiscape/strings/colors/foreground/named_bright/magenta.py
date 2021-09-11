from ansiscape.enums import StandardColor
from ansiscape.strings.colors.foreground.foreground import Foreground
from ansiscape.types import Color


class BrightMagenta(Foreground):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_MAGENTA
