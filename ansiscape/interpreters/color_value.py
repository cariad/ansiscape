from typing import List, Optional, Tuple

from ansiscape.b8 import get_8_bit_rgb
from ansiscape.enums import InterpretationKey, StandardColor
from ansiscape.interpreters.dict_value import DictValue
from ansiscape.types import Color2


class ColorValue(DictValue[Color2]):
    def __init__(self, key: InterpretationKey, force: Optional[Color2] = None) -> None:
        super().__init__(key)
        self._force = force

    def value(self, code: List[int]) -> Tuple[Optional[Color2], int]:
        if self._force is not None:
            return self._force, 0

        if code[0] == 0:
            raise NotImplementedError("Not supported")

        if code[0] == 1:
            # Transparent:
            return (0.0, 0.0, 0.0, 0.0), 1

        if code[0] == 2:
            # 24-bit colour:
            #
            # At this point, the arguments are _so_ fluid that we have to assume
            # the entire set is up for grabs, and none are intended for
            # subsequent interpreters.

            if len(code) == 1:
                # "?;2"
                # R, G and B are optional, so this is weirdly okay.
                # Intentionally make no change.
                return None, 1

            if len(code) == 2:
                # "?;2;<colour-space>"
                # We don't support colour spaces. R, G and B are optional, so
                # this is weirdly okay. Intentionally make no change.
                return None, 2

            if len(code) == 3:
                raise Exception(f"unexpected attributes: {code}")

            if len(code) == 4:
                #     "?;2;<r>;<g>;<b>"
                return (code[1] / 255, code[2] / 255, code[3] / 255, 1.0), 4

            #     "?;2;<colour-space>;<r>;<g>;<b>;<more-unsupported>"
            return (code[2] / 255, code[3] / 255, code[4] / 255, 1.0), 4

        if code[0] == 3:
            raise NotImplementedError("Cyan-Magenta-Yellow schema not supported")

        if code[0] == 4:
            raise NotImplementedError("Cyan-Magenta-Yellow-Black schema not supported")

        if code[0] == 5:
            # 8-bit colour:
            if not 0 <= code[2] <= 255:
                raise ValueError(f"argument [2] ({code[2]}) must be 0-255 inclusive")

            if code[1] == 0:
                return StandardColor.BLACK, 2
            if code[1] == 1:
                return StandardColor.RED, 2
            if code[1] == 2:
                return StandardColor.GREEN, 2
            if code[1] == 3:
                return StandardColor.YELLOW, 2
            if code[1] == 4:
                return StandardColor.BLUE, 2
            if code[1] == 5:
                return StandardColor.MAGENTA, 2
            if code[1] == 6:
                return StandardColor.CYAN, 2
            if code[1] == 7:
                return StandardColor.WHITE, 2

            if code[1] == 8:
                return StandardColor.BRIGHT_BLACK, 2
            if code[1] == 9:
                return StandardColor.BRIGHT_RED, 2
            if code[1] == 10:
                return StandardColor.BRIGHT_GREEN, 2
            if code[1] == 11:
                return StandardColor.BRIGHT_YELLOW, 2
            if code[1] == 12:
                return StandardColor.BRIGHT_BLUE, 2
            if code[1] == 13:
                return StandardColor.BRIGHT_MAGENTA, 2
            if code[1] == 14:
                return StandardColor.BRIGHT_CYAN, 2
            if code[1] == 15:
                return StandardColor.BRIGHT_WHITE, 2

            return (*get_8_bit_rgb(code[2]), 1.0), len(code)

        raise Exception("unhandled extended color")
