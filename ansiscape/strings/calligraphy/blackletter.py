from ansiscape.enums import Calligraphy
from ansiscape.strings.calligraphy.calligraphy import CalligraphyStringWithCodes


class Blackletter(CalligraphyStringWithCodes):
    @property
    def calligraphy(self) -> Calligraphy:
        return Calligraphy.BLACKLETTER
