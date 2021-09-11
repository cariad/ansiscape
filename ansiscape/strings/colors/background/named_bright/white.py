from ansiscape.enums import StandardColor
from ansiscape.strings.colors.background.background import Background
from ansiscape.types import Color


class BrightWhiteBackground(Background):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_WHITE