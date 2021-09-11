from ansiscape.enums import InterpretationKey, SelectGraphicRendition
from ansiscape.sequencers.color import ColorSequencer


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
