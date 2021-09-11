from typing import Any, Dict, List

from ansiscape.enums import (
    Blink,
    Calligraphy,
    ColorSpecial,
    Font,
    Frame,
    Ideogram,
    SelectGraphicRendition,
    StandardColor,
    Underline,
    Weight,
)
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

interpretations: Dict[SelectGraphicRendition, List[DictValue[Any]]] = {
    SelectGraphicRendition.DEFAULT: [
        BackgroundValue(ColorSpecial.DEFAULT),
        BlinkValue(Blink.NONE),
        CalligraphyValue(Calligraphy.NONE),
        ConcealValue(False),
        FontValue(Font.DEFAULT),
        ForegroundValue(ColorSpecial.DEFAULT),
        FrameValue(Frame.NONE),
        IdeogramValue(Ideogram.NONE),
        InvertValue(False),
        OverlineValue(False),
        ProportionalSpacingValue(False),
        StrikeValue(False),
        UnderlineValue(Underline.NONE),
        WeightValue(Weight.NORMAL),
    ],
    SelectGraphicRendition.BACKGROUND_BLACK: [BackgroundValue(StandardColor.BLACK)],
    SelectGraphicRendition.BACKGROUND_BLUE: [BackgroundValue(StandardColor.BLUE)],
    SelectGraphicRendition.BACKGROUND_CYAN: [BackgroundValue(StandardColor.CYAN)],
    SelectGraphicRendition.BACKGROUND_DEFAULT: [BackgroundValue(ColorSpecial.DEFAULT)],
    SelectGraphicRendition.BACKGROUND_GREEN: [BackgroundValue(StandardColor.GREEN)],
    SelectGraphicRendition.BACKGROUND_MAGENTA: [BackgroundValue(StandardColor.MAGENTA)],
    SelectGraphicRendition.BACKGROUND_RGB: [BackgroundValue()],
    SelectGraphicRendition.BACKGROUND_RED: [BackgroundValue(StandardColor.RED)],
    SelectGraphicRendition.BACKGROUND_WHITE: [BackgroundValue(StandardColor.WHITE)],
    SelectGraphicRendition.BACKGROUND_YELLOW: [BackgroundValue(StandardColor.YELLOW)],
    SelectGraphicRendition.CALLIGRAPHY_BLACKLETTER: [
        CalligraphyValue(Calligraphy.BLACKLETTER)
    ],
    SelectGraphicRendition.BLINK_FAST: [BlinkValue(Blink.FAST)],
    SelectGraphicRendition.BLINK_NONE: [BlinkValue(Blink.NONE)],
    SelectGraphicRendition.BLINK_SLOW: [BlinkValue(Blink.SLOW)],
    SelectGraphicRendition.CONCEAL_OFF: [ConcealValue(False)],
    SelectGraphicRendition.CONCEAL_ON: [ConcealValue(True)],
    SelectGraphicRendition.FONT_ALT_0: [FontValue(Font.ALT_0)],
    SelectGraphicRendition.FONT_ALT_1: [FontValue(Font.ALT_1)],
    SelectGraphicRendition.FONT_ALT_2: [FontValue(Font.ALT_2)],
    SelectGraphicRendition.FONT_ALT_3: [FontValue(Font.ALT_3)],
    SelectGraphicRendition.FONT_ALT_4: [FontValue(Font.ALT_4)],
    SelectGraphicRendition.FONT_ALT_5: [FontValue(Font.ALT_5)],
    SelectGraphicRendition.FONT_ALT_6: [FontValue(Font.ALT_6)],
    SelectGraphicRendition.FONT_ALT_7: [FontValue(Font.ALT_7)],
    SelectGraphicRendition.FONT_ALT_8: [FontValue(Font.ALT_8)],
    SelectGraphicRendition.FONT_DEFAULT: [FontValue(Font.DEFAULT)],
    SelectGraphicRendition.FOREGROUND_BLACK: [ForegroundValue(StandardColor.BLACK)],
    SelectGraphicRendition.FOREGROUND_BLUE: [ForegroundValue(StandardColor.BLUE)],
    SelectGraphicRendition.FOREGROUND_CYAN: [ForegroundValue(StandardColor.CYAN)],
    SelectGraphicRendition.FOREGROUND_DEFAULT: [ForegroundValue(ColorSpecial.DEFAULT)],
    SelectGraphicRendition.FOREGROUND_GREEN: [ForegroundValue(StandardColor.GREEN)],
    SelectGraphicRendition.FOREGROUND_MAGENTA: [ForegroundValue(StandardColor.MAGENTA)],
    SelectGraphicRendition.FOREGROUND_RGB: [ForegroundValue()],
    SelectGraphicRendition.FOREGROUND_RED: [ForegroundValue(StandardColor.RED)],
    SelectGraphicRendition.FOREGROUND_WHITE: [ForegroundValue(StandardColor.WHITE)],
    SelectGraphicRendition.FOREGROUND_YELLOW: [ForegroundValue(StandardColor.YELLOW)],
    SelectGraphicRendition.FRAME_CIRCLE: [FrameValue(Frame.ENCIRCLED)],
    SelectGraphicRendition.FRAME_FRAME: [FrameValue(Frame.FRAMED)],
    SelectGraphicRendition.FRAME_OFF: [FrameValue(Frame.NONE)],
    SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_OVER_OR_LEFT: [
        IdeogramValue(Ideogram.DOUBLE_LINE_OVER_OR_LEFT)
    ],
    SelectGraphicRendition.IDEOGRAM_DOUBLE_LINE_UNDER_OR_RIGHT: [
        IdeogramValue(Ideogram.DOUBLE_LINE_UNDER_OR_RIGHT)
    ],
    SelectGraphicRendition.IDEOGRAM_LINE_OVER_OR_LEFT: [
        IdeogramValue(Ideogram.LINE_OVER_OR_LEFT)
    ],
    SelectGraphicRendition.IDEOGRAM_LINE_UNDER_OR_RIGHT: [
        IdeogramValue(Ideogram.LINE_UNDER_OR_RIGHT)
    ],
    SelectGraphicRendition.IDEOGRAM_NONE: [IdeogramValue(Ideogram.NONE)],
    SelectGraphicRendition.IDEOGRAM_STRESS: [IdeogramValue(Ideogram.STRESS)],
    SelectGraphicRendition.INVERT_OFF: [InvertValue(False)],
    SelectGraphicRendition.INVERT_ON: [InvertValue(True)],
    SelectGraphicRendition.CALLIGRAPHY_NONE: [
        CalligraphyValue(Calligraphy.NONE),
    ],
    SelectGraphicRendition.CALLIGRAPHY_ITALIC: [CalligraphyValue(Calligraphy.ITALIC)],
    SelectGraphicRendition.OVERLINE_OFF: [OverlineValue(False)],
    SelectGraphicRendition.OVERLINE_ON: [OverlineValue(True)],
    SelectGraphicRendition.PROPORTIONAL_SPACING_OFF: [ProportionalSpacingValue(False)],
    SelectGraphicRendition.PROPORTIONAL_SPACING_ON: [ProportionalSpacingValue(True)],
    SelectGraphicRendition.STRIKE_OFF: [StrikeValue(False)],
    SelectGraphicRendition.STRIKE_ON: [StrikeValue(True)],
    SelectGraphicRendition.UNDERLINE_NONE: [UnderlineValue(Underline.NONE)],
    SelectGraphicRendition.UNDERLINE_SINGLE: [UnderlineValue(Underline.SINGLE)],
    SelectGraphicRendition.UNDERLINE_DOUBLE: [UnderlineValue(Underline.DOUBLE)],
    SelectGraphicRendition.WEIGHT_HEAVY: [WeightValue(Weight.HEAVY)],
    SelectGraphicRendition.WEIGHT_LIGHT: [WeightValue(Weight.LIGHT)],
    SelectGraphicRendition.WEIGHT_NORMAL: [WeightValue(Weight.NORMAL)],
}
