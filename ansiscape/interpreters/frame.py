from ansiscape.enums import Frame, InterpretationKey, SelectGraphicRendition
from ansiscape.interpreter import Interpreter


class FrameValue(Interpreter[Frame]):
    def __init__(self) -> None:
        super().__init__(
            key=InterpretationKey.FRAME,
            lookup={
                SelectGraphicRendition.DEFAULT: Frame.NONE,
                SelectGraphicRendition.FRAME_BOX: Frame.BOX,
                SelectGraphicRendition.FRAME_CIRCLE: Frame.CIRCLE,
                SelectGraphicRendition.FRAME_OFF: Frame.NONE,
            },
        )
