from abc import ABC, abstractmethod, abstractproperty
from typing import Iterator, Union

from ansiscape.types.interpretation_dict import InterpretationDict

SequencePart = Union[str, InterpretationDict, "SequenceProtocol"]


class SequenceProtocol(ABC):
    @abstractmethod
    def extend(self, *parts: SequencePart) -> "SequenceProtocol":
        ...

    @abstractproperty
    def parts(self) -> Iterator[Union[str, InterpretationDict]]:
        """
        Gets all the child strings and interpretations. Intentionally does not
        get child sequences, but their strings and interpretations instead.
        """
