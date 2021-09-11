from ansiscape.enums import StandardColor
from ansiscape.strings.colors.foreground import Foreground
from ansiscape.types import Color


class BrightYellow(Foreground):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_YELLOW
