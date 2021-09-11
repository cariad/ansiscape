from ansiscape.enums import StandardColor
from ansiscape.strings.colors.background.background import Background
from ansiscape.types import Color


class BrightYellowBackground(Background):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_YELLOW