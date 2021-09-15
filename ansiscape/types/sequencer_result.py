from typing import Optional, TypedDict

from ansiscape.types.attributes import Attributes


class SelectGraphicRenditionResult(TypedDict):
    attributes: Attributes


class SequencerResult(SelectGraphicRenditionResult, total=False):
    must_isolate: Optional[bool]
