from typing import TypeVar, Union

from ansiscape.enums import Blink, Calligraphy, Font, Frame, Ideogram, Underline, Weight
from ansiscape.types.color import Color

TInterpretableValue = TypeVar(
    "TInterpretableValue",
    bound=Union[
        bool,
        Blink,
        Calligraphy,
        Color,
        Font,
        Frame,
        Ideogram,
        Underline,
        Weight,
    ],
)
