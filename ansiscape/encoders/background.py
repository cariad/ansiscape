from ansiscape.encoders.color import ColorSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition


class BackgroundSequencer(ColorSequencer):
    @property
    def default_code(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.BACKGROUND_DEFAULT

    @property
    def rgb_code(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.BACKGROUND_RGB

    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.BACKGROUND
