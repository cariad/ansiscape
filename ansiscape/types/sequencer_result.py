from typing import Optional, TypedDict

from ansiscape.enums import SelectGraphicRendition
from ansiscape.types.attributes import Attributes


class SelectGraphicRenditionResult(TypedDict):
    sgr: SelectGraphicRendition


class SequencerResult(SelectGraphicRenditionResult, total=False):
    additional: Optional[Attributes]
    must_isolate: Optional[bool]
