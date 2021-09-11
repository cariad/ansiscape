from typing import List, Union

from ansiscape.encode import encode
from ansiscape.types import InterpretationDict


class Sequence:
    def __init__(self, *part: Union[str, "Sequence"]) -> None:
        self.parts = part

    @property
    def prefix(self) -> InterpretationDict:
        return InterpretationDict()

    @property
    def suffix(self) -> InterpretationDict:
        return InterpretationDict()

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
        return encode(*self.args)
