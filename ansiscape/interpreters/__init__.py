from ansiscape.handlers import register_interpreter
from ansiscape.interpreters.background import BackgroundValue
from ansiscape.interpreters.blink import BlinkValue
from ansiscape.interpreters.calligraphy import CalligraphyValue
from ansiscape.interpreters.conceal import ConcealValue
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


def register_interpreters() -> None:
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
