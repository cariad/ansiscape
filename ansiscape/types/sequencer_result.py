from typing import Optional, TypedDict

from ansiscape.enums import SelectGraphicRendition
from ansiscape.types.attributes import Attributes


class SequencerResult(TypedDict, total=False):
    sgr: SelectGraphicRendition
    additional: Optional[Attributes]
    must_isolate: Optional[bool]
