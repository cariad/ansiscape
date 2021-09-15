from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class OverlineValue(Interpreter[bool]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.OVERLINE,
            lookup={
                SelectGraphicRendition.DEFAULT: False,
                SelectGraphicRendition.OVERLINE_ON: True,
                SelectGraphicRendition.OVERLINE_OFF: False,
            },
        )
