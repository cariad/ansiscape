from ansiscape.enums import Weight
from ansiscape.strings.weight.weight import WeightStringWithCodes


class Light(WeightStringWithCodes):
    @property
    def weight(self) -> Weight:
        return Weight.LIGHT
