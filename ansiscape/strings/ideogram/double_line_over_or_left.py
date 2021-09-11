from ansiscape.enums import Ideogram
from ansiscape.strings.ideogram.ideogram import IdeogramStringWithCodes


class DoubleLineOverOrLeft(IdeogramStringWithCodes):
    @property
    def ideogram(self) -> Ideogram:
        return Ideogram.DOUBLE_LINE_OVER_OR_LEFT
