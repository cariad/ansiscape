from ansiscape.enums import Blink
from ansiscape.strings.blink.blink import BlinkStringWithCodes


class BlinkSlow(BlinkStringWithCodes):
    @property
    def blink(self) -> Blink:
        return Blink.SLOW
