from typing import TypeVar, Union

from ansiscape.enums import (
    Blink,
    Calligraphy,
    Font,
    Frame,
    Ideogram,
    MetaInterpretation,
    Underline,
    Weight,
)
from ansiscape.types.color import Color

InterpretableValue = Union[
    bool,
    Blink,
    Calligraphy,
    Color,
    Font,
    Frame,
    Ideogram,
    MetaInterpretation,
    Underline,
    Weight,
]

TInterpretableValue = TypeVar(
    "TInterpretableValue",
    bound=InterpretableValue,
)


TCovariantInterpretableValue = TypeVar(
    "TCovariantInterpretableValue",
    bound=InterpretableValue,
    covariant=True,
)
