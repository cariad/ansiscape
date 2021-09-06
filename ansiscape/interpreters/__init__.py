from typing import Any, List

from ansiscape.interpreters.blackletter import BlackletterInterpreter
from ansiscape.interpreters.blink_speed import BlinkSpeedInterpreter
from ansiscape.interpreters.conceal import ConcealInterpreter
from ansiscape.interpreters.font_face import FontFaceInterpreter
from ansiscape.interpreters.foreground_color import ForegroundColorInterpreter
from ansiscape.interpreters.frame import FrameInterpreter
from ansiscape.interpreters.ideogram import IdeogramInterpreter
from ansiscape.interpreters.intensity import IntensityInterpreter
from ansiscape.interpreters.interpretation_dict import InterpretationDict
from ansiscape.interpreters.interpreter import Interpreter
from ansiscape.interpreters.invert import InvertInterpreter
from ansiscape.interpreters.italic import ItalicInterpreter
from ansiscape.interpreters.overline import OverlineInterpreter
from ansiscape.interpreters.proportional_spacing import ProportionalSpacingInterpreter
from ansiscape.interpreters.strike import StrikeInterpreter
from ansiscape.interpreters.underline import UnderlineInterpreter
from ansiscape.interpreters.vertical_position import VerticalPositionInterpreter

interpreters: List[Interpreter[Any]] = [
    BlackletterInterpreter(),
    BlinkSpeedInterpreter(),
    ConcealInterpreter(),
    FontFaceInterpreter(),
    ForegroundColorInterpreter(),
    FrameInterpreter(),
    IdeogramInterpreter(),
    IntensityInterpreter(),
    InvertInterpreter(),
    ItalicInterpreter(),
    OverlineInterpreter(),
    ProportionalSpacingInterpreter(),
    StrikeInterpreter(),
    UnderlineInterpreter(),
    VerticalPositionInterpreter(),
]

__all__ = [
    "BlackletterInterpreter",
    "BlinkSpeedInterpreter",
    "ConcealInterpreter",
    "FontFaceInterpreter",
    "ForegroundColorInterpreter",
    "FrameInterpreter",
    "IdeogramInterpreter",
    "IntensityInterpreter",
    "InterpretationDict",
    "interpreters",
    "InvertInterpreter",
    "ItalicInterpreter",
    "OverlineInterpreter",
    "ProportionalSpacingInterpreter",
    "StrikeInterpreter",
    "UnderlineInterpreter",
    "VerticalPositionInterpreter",
]
