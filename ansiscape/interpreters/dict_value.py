from abc import ABC, abstractmethod
from typing import Generic, Optional, Tuple

from ansiscape.enums import InterpretationKey
from ansiscape.types import Attributes, TInterpretationValue


class DictValue(ABC, Generic[TInterpretationValue]):
    def __init__(self, key: InterpretationKey) -> None:
        self.key = key

    @abstractmethod
    def value(self, attrs: Attributes) -> Tuple[Optional[TInterpretationValue], int]:
        ...
