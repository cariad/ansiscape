from typing import Any, List, Protocol, Union

from ansiscape.types.interpretation_dict import InterpretationDict

SequencePart = Union[str, InterpretationDict, "SequenceProtocol"]


class SequenceProtocol(Protocol):
    @property
    def args(self) -> List[SequencePart]:
        ...

    def __add__(self, other: Any) -> "SequenceProtocol":
        ...

    @property
    def parts(self) -> List[Union[str, InterpretationDict]]:
        """
        Gets all the child strings and interpretations. Intentionally does not
        get child sequences, but their strings and interpretations instead.
        """
