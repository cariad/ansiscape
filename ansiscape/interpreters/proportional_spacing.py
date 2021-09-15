from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class ProportionalSpacingValue(Interpreter[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.PROPORTIONAL_SPACING,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.PROPORTIONAL_SPACING_ON: True,
                SelectGraphicRendition.PROPORTIONAL_SPACING_OFF: False,
            },
        )
