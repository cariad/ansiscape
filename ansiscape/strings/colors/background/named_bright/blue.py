from ansiscape.enums import StandardColor
from ansiscape.strings.colors.background.background import Background
from ansiscape.types import Color


class BrightBlueBackground(Background):
    @property
    def color(self) -> Color:
        return StandardColor.BRIGHT_BLUE
