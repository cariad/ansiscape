from typing import Any, Iterator, List, Protocol, Union

from ansiscape.types.interpretation_dict import InterpretationDict

SequencePart = Union[str, InterpretationDict, "SequenceProtocol"]


class SequenceProtocol(Protocol):
    @property
    def args(self) -> List[SequencePart]:
        ...

    def __add__(self, other: Any) -> "SequenceProtocol":
        ...

    @property
    def children(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Yields all the child strings and interpretations. Intentionally does not
        yield child sequences, but their strings and interpretations instead.
        """
