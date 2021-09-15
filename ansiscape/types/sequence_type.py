from abc import ABC, abstractmethod, abstractproperty
from typing import Iterator, Tuple, Union

from ansiscape.types.interpretation import Interpretation

SequencePart = Union[str, Interpretation, "SequenceType"]


class SequenceType(ABC):
    """A sequence of strings, formatting interpretations and sub-sequences."""

    @abstractmethod
    def extend(self, *parts: SequencePart) -> None:
        """Extends this sequence."""

    @abstractproperty
    def flatten(self) -> Iterator[Union[str, Interpretation]]:
        """
        Gets a flat (but not reduced) list of this sequence's and child
        sequence's parts.
        """

    @abstractproperty
    def parts(self) -> Tuple[SequencePart, ...]:
        """
        Gets the internal parts of this sequence. You probably want to use
        `resolved` instead.
        """

    @abstractproperty
    def resolved(self) -> Iterator[Union[str, Interpretation]]:
        """
        Flattens child sequences and gets all strings and interpretations.
        """
