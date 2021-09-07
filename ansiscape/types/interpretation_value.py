from typing import Optional, TypeVar, Union

from ansiscape.types.color import Color

TInterpretationValue = TypeVar(
    "TInterpretationValue",
    bound=Union[bool, int, Optional[Color]],
)
