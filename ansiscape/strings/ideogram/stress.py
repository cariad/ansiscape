from ansiscape.enums import Ideogram
from ansiscape.strings.ideogram.ideogram import IdeogramStringWithCodes


class Stress(IdeogramStringWithCodes):
    @property
    def ideogram(self) -> Ideogram:
        return Ideogram.STRESS
