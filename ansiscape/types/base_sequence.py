from abc import ABC, abstractproperty
from typing import List, Union

from ansiscape.types.interpretation_dict import InterpretationDict


class BaseSequence(ABC):
    @abstractproperty
    def args(self) -> List[Union[str, InterpretationDict]]:
        ...
