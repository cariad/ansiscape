from ansiscape.enums import StandardColor
from ansiscape.strings.colors.background.background import Background
from ansiscape.types import Color


class BrightCyanBackground(Background):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_CYAN
