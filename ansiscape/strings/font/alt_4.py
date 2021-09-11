from ansiscape.enums import Font
from ansiscape.strings.font.font import AlternateFont


class AlternativeFont4(AlternateFont):
    @property
    def font(self) -> Font:
        return Font.ALT_4
