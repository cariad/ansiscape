from abc import ABC, abstractmethod
from typing import Generic, List, Optional, Tuple

from ansiscape.enums import InterpretationKey
from ansiscape.types import TInterpretationValue


class DictValue(ABC, Generic[TInterpretationValue]):
    def __init__(self, key: InterpretationKey) -> None:
        self.key = key

    @abstractmethod
    def value(self, code: List[int]) -> Tuple[Optional[TInterpretationValue], int]:
        ...
