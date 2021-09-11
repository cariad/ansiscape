from ansiscape.enums import StandardColor
from ansiscape.strings.colors.foreground import Foreground
from ansiscape.types import Color


class BrightBlack(Foreground):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_BLACK
