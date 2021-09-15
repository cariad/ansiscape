from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class InvertValue(Interpreter[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.INVERT,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.INVERT_ON: True,
                SelectGraphicRendition.INVERT_OFF: False,
            },
        )
