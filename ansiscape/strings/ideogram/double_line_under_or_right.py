from ansiscape.enums import Ideogram
from ansiscape.strings.ideogram.ideogram import IdeogramStringWithCodes


class DoubleLineUnderOrRight(IdeogramStringWithCodes):
    @property
    def ideogram(self) -> Ideogram:
        return Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT
