from ansiscape.enums import Ideogram
from ansiscape.strings.ideogram.ideogram import IdeogramStringWithCodes


class SingleLineUnderOrRight(IdeogramStringWithCodes):
    @property
    def ideogram(self) -> Ideogram:
        return Ideogram.SINGLE_LINE_UNDER_OR_RIGHT
