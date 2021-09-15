from ansiscape.enums import Blink, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class BlinkValue(Interpreter[Blink]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.BLINK,
            lookup={
                SelectGraphicRendition.DEFAULT: Blink.NONE,
                SelectGraphicRendition.BLINK_SLOW: Blink.SLOW,
                SelectGraphicRendition.BLINK_FAST: Blink.FAST,
                SelectGraphicRendition.BLINK_NONE: Blink.NONE,
            },
        )
