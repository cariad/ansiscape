from typing import List, Protocol, Union

from ansiscape.types.interpretation_dict import InterpretationDict


class SequenceProtocol(Protocol):
    @property
    def args(self) -> List[Union[str, InterpretationDict]]:
        ...
