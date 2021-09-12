from ansiscape.enums import Frame, InterpretationKey
from ansiscape.enums.select_graphic_rendition import SelectGraphicRendition
from ansiscape.interpreters.dict_value import DictValue


class FrameValue(DictValue[Frame]):
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
