from ansiscape.enums import Underline
from ansiscape.strings.underline.underline import UnderlineStringWithCodes


class SingleUnderline(UnderlineStringWithCodes):
    @property
    def underline(self) -> Underline:
        return Underline.SINGLE
