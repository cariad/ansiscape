from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class StrikeValue(Interpreter[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.STRIKE,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.STRIKE_ON: True,
                SelectGraphicRendition.STRIKE_OFF: False,
            },
        )
