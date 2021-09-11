from ansiscape.encoders.bool import BoolSequencer
from ansiscape.enums import InterpretationKey, SelectGraphicRendition


class ConcealSequencer(BoolSequencer):
    @property
    def key(self) -> InterpretationKey:
        return InterpretationKey.CONCEAL

    @property
    def off(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.CONCEAL_OFF

    @property
    def on(self) -> SelectGraphicRendition:
        return SelectGraphicRendition.CONCEAL_ON
