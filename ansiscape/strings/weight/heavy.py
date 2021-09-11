from ansiscape.enums import Weight
from ansiscape.strings.weight.weight import WeightStringWithCodes


class Heavy(WeightStringWithCodes):
    @property
    def weight(self) -> Weight:
        return Weight.HEAVY
