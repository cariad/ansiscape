from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class ConcealValue(Interpreter[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.CONCEAL,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.CONCEAL_ON: True,
                SelectGraphicRendition.CONCEAL_OFF: False,
            },
        )
