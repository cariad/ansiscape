from ansiscape.enums import Frame
from ansiscape.strings.frame.frame import FrameStringWithCodes


class Box(FrameStringWithCodes):
    @property
    def frame(self) -> Frame:
        return Frame.BOX
