from ansiscape.enums import Frame, InterpretationKey
from ansiscape.interpreters.single_value import SingleValue


class FrameValue(SingleValue[Frame]):
    def __init__(self, value: Frame) -> None:
        super().__init__(InterpretationKey.FRAME, value)
