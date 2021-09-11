from ansiscape.enums import Ideogram
from ansiscape.strings.ideogram.ideogram import IdeogramStringWithCodes


class SingleLineOverOrLeft(IdeogramStringWithCodes):
    @property
    def ideogram(self) -> Ideogram:
        return Ideogram.SINGLE_LINE_OVER_OR_LEFT
