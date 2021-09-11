from ansiscape.encoders.color import ColorSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition


class ForegroundSequencer(ColorSequencer):
    @property
    def default_code(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.FOREGROUND_DEFAULT

    @property
    def rgb_code(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.FOREGROUND_RGB

    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.FOREGROUND
