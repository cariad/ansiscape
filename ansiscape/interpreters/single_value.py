from typing import Optional, Tuple

from ansiscape.enums import InterpretationKey
from ansiscape.interpreters.dict_value import DictValue
from ansiscape.types import Attributes, TInterpretationValue


class SingleValue(DictValue[TInterpretationValue]):
    def __init__(self, key: InterpretationKey, value: TInterpretationValue) -> None:
        super().__init__(key)
        self._value = value

    def value(self, attrs: Attributes) -> Tuple[Optional[TInterpretationValue], int]:
        return self._value, 0
