from ansiscape.enums import Font
from ansiscape.strings.font.font import AlternateFont


class AlternateFont1(AlternateFont):
    @property
    def font(self) -> Font:
        return Font.ALT_1
