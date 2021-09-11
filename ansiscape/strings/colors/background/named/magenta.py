from ansiscape.enums import StandardColor
from ansiscape.strings.colors.background.background import Background
from ansiscape.types import Color


class MagentaBackground(Background):
    @property
    def color(self) -> Color:
        return StandardColor.MAGENTA
