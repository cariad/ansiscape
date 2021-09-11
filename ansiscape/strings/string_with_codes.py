from abc import ABC, abstractproperty
from typing import List, Union

from ansiscape.sequencers import to_string
from ansiscape.types import InterpretationDict


class StringWithCodes(ABC):
    def __init__(self, *part: Union[str, "StringWithCodes"]) -> None:
        self.parts = part

    @abstractproperty
    def prefix(self) -> InterpretationDict:
        ...

    @abstractproperty
    def suffix(self) -> InterpretationDict:
        ...

    @property
    def args(self) -> List[Union[str, InterpretationDict]]:
        args: List[Union[str, InterpretationDict]] = [self.prefix]

        for part in self.parts:
            if isinstance(part, str):
                args.append(part)
            else:
                args.extend(part.args)

        args.append(self.suffix)
        return args

    def __str__(self) -> str:
        return to_string(*self.args)
