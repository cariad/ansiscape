from typing import Any, Dict, List

from ansiscape.enums import SelectGraphicRendition
from ansiscape.handlers import register_interpreter
from ansiscape.interpreters.background import BackgroundValue
from ansiscape.interpreters.blink import BlinkValue
from ansiscape.interpreters.calligraphy import CalligraphyValue
from ansiscape.interpreters.conceal import ConcealValue
from ansiscape.interpreters.dict_value import DictValue
from ansiscape.interpreters.font import FontValue
from ansiscape.interpreters.foreground import ForegroundValue
from ansiscape.interpreters.frame import FrameValue
from ansiscape.interpreters.ideogram import IdeogramValue
from ansiscape.interpreters.invert import InvertValue
from ansiscape.interpreters.overline import OverlineValue
from ansiscape.interpreters.proportional_spacing import ProportionalSpacingValue
from ansiscape.interpreters.strike import StrikeValue
from ansiscape.interpreters.underline import UnderlineValue
from ansiscape.interpreters.weight import WeightValue

register_interpreter(BackgroundValue())
register_interpreter(BlinkValue())
register_interpreter(CalligraphyValue())
register_interpreter(ConcealValue())
register_interpreter(FontValue())
register_interpreter(ForegroundValue())
register_interpreter(FrameValue())
register_interpreter(IdeogramValue())
register_interpreter(InvertValue())
register_interpreter(OverlineValue())
register_interpreter(ProportionalSpacingValue())
register_interpreter(StrikeValue())
register_interpreter(UnderlineValue())
register_interpreter(WeightValue())

interpretations: Dict[SelectGraphicRendition, List[DictValue[Any]]] = {
    SelectGraphicRendition.DEFAULT: [
        BackgroundValue(),
        BlinkValue(),
        CalligraphyValue(),
        ConcealValue(),
        FontValue(),
        ForegroundValue(),
        FrameValue(),
        IdeogramValue(),
        InvertValue(),
        OverlineValue(),
        ProportionalSpacingValue(),
        StrikeValue(),
        UnderlineValue(),
        WeightValue(),
    ],
    SelectGraphicRendition.BACKGROUND_BLACK: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_BLUE: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_CYAN: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_DEFAULT: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_GREEN: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_MAGENTA: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_RGB: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_RED: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_WHITE: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_YELLOW: [BackgroundValue()],
    SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER: [CalligraphyValue()],
    SelectGraphicRendition.BLINK_FAST: [BlinkValue()],
    SelectGraphicRendition.BLINK_NONE: [BlinkValue()],
    SelectGraphicRendition.BLINK_SLOW: [BlinkValue()],
    SelectGraphicRendition.CONCEAL_OFF: [ConcealValue()],
    SelectGraphicRendition.CONCEAL_ON: [ConcealValue()],
    SelectGraphicRendition.FONT_ALT_0: [FontValue()],
    SelectGraphicRendition.FONT_ALT_1: [FontValue()],
    SelectGraphicRendition.FONT_ALT_2: [FontValue()],
    SelectGraphicRendition.FONT_ALT_3: [FontValue()],
    SelectGraphicRendition.FONT_ALT_4: [FontValue()],
    SelectGraphicRendition.FONT_ALT_5: [FontValue()],
    SelectGraphicRendition.FONT_ALT_6: [FontValue()],
    SelectGraphicRendition.FONT_ALT_7: [FontValue()],
    SelectGraphicRendition.FONT_ALT_8: [FontValue()],
    SelectGraphicRendition.FONT_DEFAULT: [FontValue()],
    SelectGraphicRendition.FOREGROUND_BLACK: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_BLUE: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_CYAN: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_DEFAULT: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_GREEN: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_MAGENTA: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_RGB: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_RED: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_WHITE: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_YELLOW: [ForegroundValue()],
    SelectGraphicRendition.FRAME_CIRCLE: [FrameValue()],
    SelectGraphicRendition.FRAME_BOX: [FrameValue()],
    SelectGraphicRendition.FRAME_OFF: [FrameValue()],
    SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT: [IdeogramValue()],
    SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT: [IdeogramValue()],
    SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_OVER_OR_LEFT: [IdeogramValue()],
    SelectGraphicRendition.IDEOGRAM_SINGLE_LINE_UNDER_OR_RIGHT: [IdeogramValue()],
    SelectGraphicRendition.IDEOGRAM_NONE: [IdeogramValue()],
    SelectGraphicRendition.IDEOGRAM_STRESS: [IdeogramValue()],
    SelectGraphicRendition.INVERT_OFF: [InvertValue()],
    SelectGraphicRendition.INVERT_ON: [InvertValue()],
    SelectGraphicRendition.CALLIGRAPHY_NONE: [
        CalligraphyValue(),
    ],
    SelectGraphicRendition.CALLIGRAPHY_ITALIC: [CalligraphyValue()],
    SelectGraphicRendition.OVERLINE_OFF: [OverlineValue()],
    SelectGraphicRendition.OVERLINE_ON: [OverlineValue()],
    SelectGraphicRendition.PROPORTIONAL_SPACING_OFF: [ProportionalSpacingValue()],
    SelectGraphicRendition.PROPORTIONAL_SPACING_ON: [ProportionalSpacingValue()],
    SelectGraphicRendition.STRIKE_OFF: [StrikeValue()],
    SelectGraphicRendition.STRIKE_ON: [StrikeValue()],
    SelectGraphicRendition.UNDERLINE_NONE: [UnderlineValue()],
    SelectGraphicRendition.UNDERLINE_SINGLE: [UnderlineValue()],
    SelectGraphicRendition.UNDERLINE_DOUBLE: [UnderlineValue()],
    SelectGraphicRendition.WEIGHT_HEAVY: [WeightValue()],
    SelectGraphicRendition.WEIGHT_LIGHT: [WeightValue()],
    SelectGraphicRendition.WEIGHT_NORMAL: [WeightValue()],
}
